French version Below

# Heart-Disease-Prediction
Heart Disease Angiographic Prediction /  Prediction Maladie Caridiaque résultat angiographique
This is an implementation of 3 machine learning algorithms for demonstration purpose to medical staff in a French Hospital.
ML implementation structure is directly inspired from the project [Heart_Disease_Prediction](https://github.com/bveber/Heart_Disease_Prediction) by [Brandon Veber](https://github.com/bveber). 
The GUI has been re-written in Python using tkinter GUI toolkit. 
The GUI is in French. Values can be initialized with 4 examples samples. This has been added for demonstration purpose.

Nota Bene : The result of the prediction is given in a box that asks the user (doctor) to validate or not the prediction. This has been made for eductationnal purpose, to show the doctors how they could improve the existing model by adding their data. Their is no implementation behind. (even if it would not be difficult). There is no plan to add one.

To run, run GUI.py with python3. Some librairies may be needed.

Author: Cyril de Catheu
Created: 31-03-2018
Last Modified: 31-03-2018
Tested on OS X Sierra, Windows 8

# Requires:
Python >= 3.4.1:
	Python package dependencies:
		sklearn >= 0.16.1
		numpy   >= 1.9.0
		pandas  >= 0.15.0

# Prediction Technical Specifications:
## Data:
	The data is from the UCI Machine Learning Repository Heart Disease Data Set.
	https://archive.ics.uci.edu/ml/datasets/Heart+Disease
	procesessed.cleveland.data contains 303 samples with 13 input features, and target value.
	procesessed.all.data contains 920 samples. Data is a bit more sparse.

 
## Input Features :
	Age - real number
	Sex - categorical
	Chest pain type - categorical
	Resting blood pressure - real number
	Serum cholesterol - real number
	Fasting blood sugar - real number (internally converted to categorical)
	Resting ECG results - categorical
	Maximum achievable heart rate - real number
	Exercised induced angina - categorical
	ST depression induced by exercise relative to rest - real number
	Slope of the peak exercise ST segment - categorical
	Number of major vessels colored by floroscopy - real number
	Thallium heart scan - categorical

## Feature encoding:
	All categorical features are converted to binary using a 
	one-hot encoder

## Feature normalization:
	All real numbers are scaled using a standard scaler (subtract mean
	and divide by standard deviation)

## Machine Learning Algorithm:
### SVM Classifier
	A radial basis kernel SVM classifier is used for making predictions.
	The output is a probability representing the likelihood of the 
	presence of heart disease.

	Expected Accuray: processed.cleveland.data
		The data was tested using a 10-fold cross validation technique.
		The results are:

		Avg Accuracy   Avg Recall     Avg Precision  Avg ROC_AUC
		0.842          0.792          0.863          0.932
