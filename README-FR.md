
La version anglaise peut être trouvé dans le [README.md](README.md)

# Heart-Disease-Prediction
Prédiction de Maladie cardiaque : résultat d'une angiographie.
Implémentation de 3 algorithmes de classifcation dans le but pour réaliser une démonstration à des équipes médicales d'un hopital en France.  
La documentation de ce projet peut être trouvée dans [documentation ](/documentation).
La structure de l'implémentation des classificateurs est directement inspirée du projet [Heart_Disease_Prediction](https://github.com/bveber/Heart_Disease_Prediction) de [Brandon Veber](https://github.com/bveber).  
L'interface graphique a été réécrite en Python en utilisant la bibilothèque graphique tkinter.  
L'interface est en français. Les valeurs peuvent être initialisées par 4 exemples de patient.

Nota Bene : Le résultat de la predition est donné dans une boîte de dialogue qui demande à l'utilisateur (médecin) de confirmer ou non la prediction. Cela a été fait dans un but éducatif, pour montrer aux médecins qu'ils pourront améliorer le modèle en ajoutant leur données. Il n'est pas prévu d'en réaliser une (bien que cela soit simple).

Nota Bene 2 : le code est fortement dupliqué pour les 3 algorithmes de classification, et pourrait être refactorisé.

Pour lancer l'interface, exécuter GUI.py avec python3.

Auteur: Cyril de Catheu  
Création: 31-03-2018  
Dernière modification: 31-03-2018  
Testé sur OS X Sierra, Windows 8  

## Requirements:
Python >= 3.4.1: 
	Librairies:  
		sklearn >= 0.16.1  
		numpy   >= 1.9.0  
		pandas  >= 0.15.0   

## Spécification Technique de la prédiction:
### Données:
	Les données proviennent de l'UCI Machine Learning Repository Heart Disease Data Set: 
	https://archive.ics.uci.edu/ml/datasets/Heart-Disease
	procesessed.cleveland.data contient 303 échantillons labelisés de 13 features.
	procesessed.all.data contient 920 échnatillons. Les échantillons sont plus incomplets.

 
### Features :
	Age - Réel
	Sex - Nominale
	Chest pain type - Nominale
	Resting blood pressure - Réel
	Serum cholesterol - Réel
	Fasting blood sugar - Nominale
	Resting ECG results - Nominale
	Maximum achievable heart rate - Réel
	Exercised induced angina - Nominale
	ST depression induced by exercise relative to rest - Réel
	Slope of the peak exercise ST segment - Nominale
	Number of major vessels colored by floroscopy - Réel
	Thallium heart scan - Nominale

### Feature encoding:
	Toutes les features All categorical features are converted to binary using a 
	one-hot encoder

### Feature normalization:
	All real numbers are scaled using a standard scaler (subtract mean
	and divide by standard deviation)

### Machine Learning Algorithm:
#### SVM Classifier
	A radial basis kernel SVM classifier is used for making predictions.
	The output is a probability representing the likelihood of the 
	presence of heart disease.

	Expected Accuray: processed.cleveland.data
		The data was tested using a 10-fold cross validation technique.
		The results are:
		Avg Accuracy   Avg Recall     Avg Precision  Avg ROC_AUC
		0.842          0.792          0.863          0.932
	Expected Accuray: processed.all.data
		The data was randomly shuffled and tested using a 10-fold cross validation technique.
		The average results for 5 cross validations are:
		Avg Accuracy   Avg Recall     Avg Precision  Avg ROC_AUC
		0.827          0.872          0.825          0.891
		
#### Naive Bayes Classifier
	A Naive Bayes classifier for multivariate Bernoulli is used for making predictions.
	Please keep in mind that using this classifier for this dataset is clearly not a good choice.
	Made only for demonstration purpose : accuracy for the small dataset is quite good. 
	The output is a probability representing the likelihood of the 
	presence of heart disease.

	Expected Accuray: processed.cleveland.data
		The data was tested using a 10-fold cross validation technique.
		The results are:
		Avg Accuracy   Avg Recall     Avg Precision  Avg ROC_AUC
		0.832          0.821          0.812          0.905
	Expected Accuray: processed.all.data
		The data was randomly shuffled and tested using a 10-fold cross validation technique.
		The average results for 5 cross validations are:
		Avg Accuracy   Avg Recall     Avg Precision  Avg ROC_AUC
		0.798          0.805          0.826          0.875
		
#### Gradient Boosting Classifier
	A Gradient Boosting classifier is used for making predictions.
	This algorithm is the only one that got better results when scaling to the full dataset.
	The output is a probability representing the likelihood of the 
	presence of heart disease.

	Expected Accuray: processed.cleveland.data
		The data was tested using a 10-fold cross validation technique.
		The results are:
		Avg Accuracy   Avg Recall     Avg Precision  Avg ROC_AUC
		0.795          0.758          0.800          0.914
	Expected Accuray: processed.all.data
		The data was randomly shuffled and tested using a 10-fold cross validation technique.
		The average results for 5 cross validations are:
		Avg Accuracy   Avg Recall     Avg Precision  Avg ROC_AUC
		0.813          0.854          0.817          0.900
