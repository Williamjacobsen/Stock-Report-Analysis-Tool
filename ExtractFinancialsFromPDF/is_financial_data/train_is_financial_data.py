import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib
import re

def preprocess(text):
    text = re.sub(r'\d{4}', '<DATE>', text)
    text = re.sub(r'\d+[\.,]?\d*', '<NUM>', text)
    text = re.sub(r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*', '<DATE>', text)
    text = re.sub(r'(<NUM>/<NUM>|<DATE>/<NUM>)', '<DATE>', text)
    return text.lower()

data = pd.read_csv("../data.csv")
texts = [preprocess(t) for t in data['financial_data']]
labels = data['truth_value']

vectorizer = TfidfVectorizer(
    token_pattern=r'(?u)\b[a-zA-Z<>]+[\w<>]+\b',
    ngram_range=(1, 3)
)

X = vectorizer.fit_transform(texts)

model = LogisticRegression(class_weight='balanced')
model.fit(X, labels)

joblib.dump(vectorizer, 'vectorizer.pkl')
joblib.dump(model, 'classifier.pkl')