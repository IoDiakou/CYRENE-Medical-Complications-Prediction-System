# CYRENE-Medical-Complications-Prediction-System
A multilabel classification system for the prediction of medical complications of patients with myocardial infarction.

YOU CAN FIND THE APP HERE: https://iodiakou-cyrene.streamlit.app/

CYRENE is a sample of a predictive system in service and support of a medical professional. It allows the prediction of complications for patients who have suffered a myocardial infarction, in the context of personalized medicine and efficient patient managemenet in the hospital.

The prediction challenge is reframed as a multilabel classification problem, with labels being the potential complications. The dataset used for the training of the algorithm is the Myocardial infarction complications Data Set (https://archive.ics.uci.edu/ml/datasets/Myocardial+infarction+complications).

The algorithm used for the model is the OneVsRest classifier, wrapped in an XGBoost classifier. 

For the sake of a user-friendly study case, the web app accepts a small number of input data to carry out the prediction. 
For a more detailed view of the data preprocessing behind CYRENE, see the sister repository https://github.com/IoDiakou/MLC-on-biomedical-data
