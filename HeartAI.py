import pandas as pd
import numpy as np
from sklearn import preprocessing, svm, ensemble, neighbors, metrics, model_selection
import time
import sys, os
import pickle

#on assure le compatibilité pour Python 2 et 3
called_version = sys.version_info
if called_version[0] == 2:
    from Tkinter import Tk
    from tkFileDialog import askopenfilename
elif called_version[0] == 3:
    from tkinter import Tk,filedialog

#FIXME merger avec l'algorithme de boost et plus tard de Bayes

def main(data_string,filename="processed.all.data"):
    '''Crée ou charge un modele, normalise les données d'entrées puis réalise une prédiction'''
    #on verifie s'il y a un modele deja existant, sinon on le cree
    model_savename = filename + 'Model.p'
    if not os.path.isfile('/'.join((os.path.dirname(os.path.realpath(__file__)),model_savename))):
        faireModele(filename)

    #on ouvre le modele en format pickle, contient model, data, scaler et encoder
    modeller = pickle.load(open(model_savename,'rb')) #b pour binary, r pour read

    #on mets les données d'entrée sous forme d'array et on transtype
    inputData = data_string.split(' ')
    print(inputData)
    inputData = [[float(e) for e in inputData]] #WARNING rajout d'une dimension ici

    #on centre réduit, nécessaire pour le modele en noyau
    scaledData = normaliseTest(inputData, modeller['scaler'], modeller['encoder'])


    #on réalise la prédiction
    # le résultat est de la forme [[proba_sain, proba_malade]]
    prediction = modeller['model'].predict_proba(scaledData)  #attention les probas peuvent être mauvaises avec un peti jeu de données
    predictionSetFun = modeller['model'].decision_function(scaledData)
    predictionSet = modeller['model'].predict(scaledData)
    r1 = "%-30s%-4.2f%-1s" % ('La chance d\'avoir une sténose importante révélée par angiographie est de ', 100 * prediction[0][1], '%')
    #r2 = "%-30s%-4.2f%-1s" % ('Le patient semble être dans la catégorie : ', predictionSet[0], '.')
    if predictionSet[0] == 1:
        r2 = "Patient dans la catégorie : Sténose de plus de  50%."
    elif predictionSet[0] ==0:
        r2 = "Patient dans la catégorie : Sténose de moins de  50%."
    #r3 = "%-30s%-4.2f%-1s" % ('Distance par rapport à l\'hyperplan (plus on est éloigné de 0, plus la distance est grande): ', predictionSetFun[0], '.')
    print(r1)
    print(r2)
    #print(r3)
    return r1 + "\n" + "\n" + r2 #+ "\n" +r3


def faireModele(filename="processed.all.data"):
    '''Crée un modele depuis un fichier et sauvegarde dans un fichier pickle'''
    rawData = np.array(pd.read_csv(filename,header=None))

    data = processFeaturesTarget(rawData)
    training_scaled, scaler, encoder = normaliseTrain(data['X'])
    model = svm.SVC(probability =True).fit(training_scaled,data['y'])

    #on sauvegarde
    model_savename = filename + 'Model.p'
    pickle.dump({'model': model,'data': data,'scaler': scaler, 'encoder': encoder}, open(model_savename,'wb'))


def normalise(train, test, scalerType='Standard'):
    '''Retourne les données normalisées. Attention, seulement pour des données float.'''

    trainScaled, scaler, encoder = normaliseTrain(train)
    testScaled = normaliseTest(test, scaler, encoder)
    return (trainScaled, testScaled)

def normaliseTrain(train):
    ''' Retourne les données normalisées et le scaler. Attention seulement pour des données float'''

    # codage des valeurs categoriques, pour pouvoir les envoyer dans un modele SVM
    #auto : determine le nb de categorie, array : les features à traiter
    #sparse = False pour renvoyer un array plutot qu'une matrice
    #on n'applique pas à sexe et exercise induced angina puisqu'il n'y a que 2 catégories
    encoder = preprocessing.OneHotEncoder('auto',[2,6,10,12], sparse=False)

    features = encoder.fit_transform(train)

    #on met sous forme supervisée
    realValueIndex = 13
    realValuedData = features[:, realValueIndex:]

    #on normalise selon la méthode standard (moyenne et ecart type):
    scaler = preprocessing.StandardScaler()
    scaledData = scaler.fit_transform(realValuedData)


    # on renvoie les features encodée correctement
    return np.hstack((features[:,:realValueIndex],scaledData)),scaler,encoder


def normaliseTest(test, scaler, encoder):
    '''Prend en argument les infos pour scaler et les applique au jeux de données de test'''

    #encodage des valeurs categoriques
    features = encoder.transform(test)

    #on met sous forme supervisée
    realValueIndex = 13
    realValuedData = features[:, realValueIndex:]
    scaledData = scaler.transform(realValuedData)
    return np.hstack((features[:, :realValueIndex], scaledData))


def processFeaturesTarget(inputData):
    """Separe les features en entrée et le label attendu
    On enleve la distinction des maladies aussi, on ne garde que accident ou pas accident"""

    #copie de l'inputData
    inputDataWork = inputData.copy()

    # on remplace les ? des valeurs manquantes en nan pis en convertis en float
    inputDataWork[inputDataWork == '?'] = np.nan
    inputDataWork.astype(np.float)

    #on remplace les valeurs manquantes par les valeurs les plus fréquentes
    features = preprocessing.Imputer(strategy='most_frequent').fit_transform(inputDataWork[:, :-1])

    # On enleve la distinction des maladies, >1 prend la valeur 1
    #le jeu est trop petit pour esperer avoir des résultats satisfaisants en gardant les distinctions de maladie
    inputDataWork[:, -1][inputDataWork[:, -1] >= 1] = 1
    return ({'X': features, 'y': np.array(inputDataWork[:, -1], dtype='f')})



def analyse(verbose=0,filename = "processed.all.data", shuffling=True ):
    ''' Réalise l'analyse des résultats'''

    t0 = time.time()

    # FIXME nom du fichier codé en dur sans defaulting
    rawdata = np.array(pd.read_csv(filename,header=None))
    data = processFeaturesTarget(rawdata)

    score = crossValidation(data, verbose, shuffling)
    if verbose >= 0:
        print("%-15s%-15s%-15s%-15s" % ('Moy Accuracy', 'Moy Recall', 'Moy Precision', 'Moy ROC_AUC'))
        print("%-15.3f%-15.3f%-15.3f%-15.3f" % (np.mean(score[0]), np.mean(score[1]), np.mean(score[2]), np.mean(score[3])))
    print('Runtime is ', time.time() - t0, '(s)')
    return score

def crossValidation(data, verbose=0, shuffling=True):
    "10-fold validation"

    kf = model_selection.KFold(n_splits=10, shuffle=shuffling)

    accuracies = np.array([])
    recalls = np.array([])
    precisions = np.array([])
    rocs = np.array([])
    numFold = 1
    for train_index, test_index in kf.split(data['X']):
        X_train, X_test = data['X'][train_index], data['X'][test_index]
        y_train, y_test = data['y'][train_index], data['y'][test_index]
        X_train, X_test = normalise(X_train, X_test)


        #on trouve le meilleur estimateur
        clf = model_selection.GridSearchCV(
            svm.SVC(probability=True), {'C': [1], 'kernel': ['rbf']}
        ).fit(X_train, y_train)

        #on affiche l'estimateur si on a un haut niveau de verbose
        if verbose>3:print(clf.best_estimator_)
        #on utilise l'estimateur sur tout le jeu de test
        preds = clf.predict(X_test)
        predsProb = clf.predict_proba(X_test)

        #on affiche le label et la proba attribuée à la valeur malade pour toutes les lignes testées
        if verbose>2:
            comp=[[y_test[i],predsProb[i,1]] for i in range(len(y_test))]
            for row in comp: print(row)

        #on crée les metriques et on les ajoute a la liste des metriques mesurés
        roc = metrics.roc_auc_score(y_test, predsProb[:, 1])
        acc = metrics.accuracy_score(y_test, preds)
        recall = metrics.recall_score(y_test, preds)
        precision = metrics.precision_score(y_test, preds)
        rocs = np.append(rocs, roc)
        accuracies = np.append(accuracies, acc)
        recalls = np.append(recalls, recall)
        precisions = np.append(precisions, precision)

        #on affiche les métriques pour le fold si verbose
        if verbose>1:
            print('%-15s%-15s%-15s%-15s%-15s'%('Fold','Accuracy','Recall','Precision','ROC_AUC'))
            print('%-15.3f%-15.3f%-15.3f%-15.3f%-15.3f'%(numFold,acc,recall,precision,roc))
        numFold += 1

    #on renvoie la moyenne des métriques
    return (np.array((accuracies, recalls, precisions, roc)))


#FIXME : décommenté pour ne pas être lancé lors de l'import par le fichier GUI, il faut mettre ces lignes dans un autre fichier
#main("62.0 0.0 4.0 140.0 268.0 0.0 2.0 160.0 0.0 3.6 3.0 2.0 3.0")
#main("62.0 0.0 4.0 140.0 268.0 0.0 2.0 160.0 0.0 3.6 3.0 2.0 3.0","processed.cleveland.data")
#main("44.0 1.0 2.0 120.0 263.0 0.0 0.0 173.0 0.0 0.0 1.0 0.0 7.0")
#main("44.0 1.0 2.0 120.0 263.0 0.0 0.0 173.0 0.0 0.0 1.0 0.0 7.0","processed.cleveland.data")

analyse(1)
#analyse(1,"processed.cleveland.data",False)