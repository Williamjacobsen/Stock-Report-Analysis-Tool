import joblib
import re
import os

def preprocess(text):
    text = re.sub(r'\d{4}', '<DATE>', text)
    text = re.sub(r'\d+[\.,]?\d*', '<NUM>', text)
    text = re.sub(r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*', '<DATE>', text)
    text = re.sub(r'(<NUM>/<NUM>|<DATE>/<NUM>)', '<DATE>', text)
    return text.lower()

current_dir = os.path.dirname(__file__)
vectorizer = joblib.load(os.path.join(current_dir, 'vectorizer.pkl'))
model = joblib.load(os.path.join(current_dir, 'classifier.pkl'))

def is_financial_data(text):
    processed = preprocess(text)

    text_vector = vectorizer.transform([processed])

    prediction = model.predict(text_vector)

    confidence = model.predict_proba(text_vector)[0][prediction[0]]
    return prediction[0] == 1, confidence