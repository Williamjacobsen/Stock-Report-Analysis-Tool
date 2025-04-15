import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

data = pd.read_csv("data.csv")
texts = data['Input']
labels = data['Value']

vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(texts)

model = LogisticRegression(class_weight='balanced')
model.fit(X, labels)

joblib.dump(vectorizer, 'vectorizer.pkl')
joblib.dump(model, 'classifier.pkl')