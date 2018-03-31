
La version anglaise peut être trouvé dans le [README.md](README.md)

# Heart-Disease-Prediction
Prédiction de Maladie cardiaque : résultat d'une angiographie.
Implémentation de 3 algorithmes de classification dans le but de réaliser une démonstration à des équipes médicales d'un hopital en France.  
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

## Requirements :
Python >= 3.4.1: 
	Librairies:  
		sklearn >= 0.16.1  
		numpy   >= 1.9.0  
		pandas  >= 0.15.0   

## Spécification Techniques de la prédiction :
### Données:
	Les données proviennent de l'UCI Machine Learning Repository Heart Disease Data Set: 
	https://archive.ics.uci.edu/ml/datasets/Heart-Disease
	procesessed.cleveland.data contient 303 échantillons labelisés de 13 features.
	procesessed.all.data contient 920 échnatillons. Les échantillons sont plus incomplets.

 
### Features :
	Age - Réel
	Sexe - Nominale
	Type de douleur à la poitrine - Nominale
	Pression sanguine au repos - Réel
	Choléstérol Sérique - Réel
	Glycémie à jeun - Nominale
	ECG au repos - Nominale
	Fréquence Cardiaque Maximale - Réel
	Angine induite par l'effort - Nominale
	Sous-décalage du segment S-T - Réel (revoir traduction fr)
	Pente au sommet du segment S-T pendant l'effort - Nominale
	Nombre de vaisseaux principaux colorés par fluoroscopie/radioscopie - Réel
	Examen du coeur au thallium - Nominale

### Encodage des Features :
	Toutes les features nominales sont converties en binaire avec un encodage one-hot.

### Normalisation des Feature :
	Les features réelles sont centrée-réduites.

### Algorithme d'Intelligence Artificielle :
#### SVM Classifier
	Un classificateur SVM est utilisé.
	Le résultat est une probabilité que le patient ait un résultat d'angiographie révélant une sténose de plus de 50%.

	Dataset : processed.cleveland.data
		Les données ont été testées en 10-fold cross validation
		Résultats :
		Avg Accuracy   Avg Recall     Avg Precision  Avg ROC_AUC
		0.842          0.792          0.863          0.932
	Dataset : processed.all.data
		Les données ont été mélangé aléatoirement puis testées en 10-fold cross validation.
		Résultats moyens pour 5 cross-validations :
		Avg Accuracy   Avg Recall     Avg Precision  Avg ROC_AUC
		0.827          0.872          0.825          0.891
		
#### Naive Bayes Classifier
	Un modèle bayésien naif à multiple Bernoulliest utilisé.
	Noter que ce modèle n'est évidemment pas un bon choix pour ce problème.
	Made only for demonstration purpose : accuracy for the small dataset is quite good. 
	Le résultat est une probabilité que le patient ait un résultat d'angiographie révélant une sténose de plus de 50%.

	Dataset : processed.cleveland.data
		Les données ont été testées en 10-fold cross validation
		Résultats :
		Avg Accuracy   Avg Recall     Avg Precision  Avg ROC_AUC
		0.832          0.821          0.812          0.905
	Dataset : processed.all.data
		Les données ont été mélangé aléatoirement puis testées en 10-fold cross validation.
		Résultats moyens pour 5 cross-validations :
		Avg Accuracy   Avg Recall     Avg Precision  Avg ROC_AUC
		0.798          0.805          0.826          0.875
		
#### Gradient Boosting Classifier
	A Gradient Boosting classifier is used for making predictions.
	This algorithm is the only one that got better results when scaling to the full dataset.
	Le résultat est une probabilité que le patient ait un résultat d'angiographie révélant une sténose de plus de 50%.

	Dataset : processed.cleveland.data
		Les données ont été testées en 10-fold cross validation
		Résultats :
		Avg Accuracy   Avg Recall     Avg Precision  Avg ROC_AUC
		0.795          0.758          0.800          0.914
	Dataset : processed.all.data
		Les données ont été mélangé aléatoirement puis testées en 10-fold cross validation.
		Résultats moyens pour 5 cross-validations :
		Avg Accuracy   Avg Recall     Avg Precision  Avg ROC_AUC
		0.813          0.854          0.817          0.900
		
## Next Steps :	
Essayer avec les algorithme R* et LogitBoost
