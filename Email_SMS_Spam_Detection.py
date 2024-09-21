import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import SVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score, classification_report

from google.colab import files
uploaded = files.upload()

dataset = pd.read_csv('spam.csv', encoding='latin-1')

print(dataset)

message = dataset['v2'].tolist()
category = dataset['v1'].to_numpy()

X_train, X_test, y_train, y_test = train_test_split(message, category, test_size=0.2, random_state=42)

vectorizer = CountVectorizer()
X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)

svm_classifier = SVC(kernel='linear', probability=True)
naive_bayes_classifier = MultinomialNB()

voting_classifier = VotingClassifier(estimators=[('svm', svm_classifier), ('naive_bayes', naive_bayes_classifier)], voting='soft')

voting_classifier.fit(X_train_vectorized, y_train)

predictions = voting_classifier.predict(X_test_vectorized)

accuracy = accuracy_score(y_test, predictions)
classification_report_result = classification_report(y_test, predictions)
print("Accuracy:", accuracy)
print("Classification Report:\n", classification_report_result)

def predict_message(message):
    message_vectorized = vectorizer.transform([message])
    prediction = voting_classifier.predict(message_vectorized)
    return prediction[0]

input_message = input("Enter a message to check if it's ham or spam: ")
result = predict_message(input_message)
print("The message is:", result)
