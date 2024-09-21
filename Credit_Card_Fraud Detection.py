#Link to dataset: https://www.kaggle.com/datasets/nelgiriyewithana/credit-card-fraud-detection-dataset-2023
#Could not upload the dataset in Git because the size was large.

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score, classification_report

credit = pd.read_csv('/content/creditcard_2023.csv')

print(credit)

print(credit.isna().sum()) #to check if dataset has null values or not
credit = credit.dropna()
print("Dataset after removing NaN values:")
print(credit)

legitimate = credit[credit.Class == 0]
fraudulent = credit[credit.Class == 1]
print(legitimate.Amount.describe())
print(fraudulent.Amount.describe())

legitimate_sample = legitimate.sample(n=len(fraudulent)) #this is done because value of fraudulent activity gets changed in some time. 

new_dataset = pd.concat([legitimate_sample, fraudulent], axis=0)
new_dataset.head()

new_dataset['Class'].value_counts()

legitimate = new_dataset[new_dataset.Class == 0]
fraudulent = new_dataset[new_dataset.Class == 1]

print(legitimate.shape)
print(fraudulent.shape)

legitimate.Amount.describe()
fraudulent.Amount.describe()

#comparing the values for both transactions in new dataset.
new_dataset.groupby('Class').mean()

X = new_dataset.drop(columns='Class', axis=1)
Y = new_dataset['Class']

print(Y)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)

print(X.shape,X_train.shape,X_test.shape)

model_1 = LogisticRegression()
model_2 = SVC(probability=True)
en_model = VotingClassifier(estimators=[('logistic', model_1), ('svm', model_2)], voting='soft')
en_model.fit(X_train, Y_train)

X_train_prediction = en_model.predict(X_train)

accuracy = accuracy_score(X_train_prediction, Y_train)
print(f'Accuracy: ',accuracy*100,'%')
train_classification_report = classification_report(Y_train, X_train_prediction)
print('Training Classification Report:')
print(train_classification_report)

X_test_prediction = en_model.predict(X_test)

accuracy = accuracy_score(X_test_prediction, Y_test)
print(f'Accuracy: ',accuracy*100,'%')
test_classification_report = classification_report(Y_test, X_test_prediction)
print('Testing Classification Report:')
print(test_classification_report)
