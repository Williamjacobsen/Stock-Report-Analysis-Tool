import joblib
import os

current_dir = os.path.dirname(__file__)
vectorizer = joblib.load(os.path.join(current_dir, 'vectorizer.pkl'))
model = joblib.load(os.path.join(current_dir, 'classifier.pkl'))

def is_topic_prediction(text):
    text_vector = vectorizer.transform([text])

    prediction = model.predict(text_vector)

    confidence = model.predict_proba(text_vector)[0][prediction[0]]
    return prediction[0] == 1, confidence

def is_topic(line):
    line = line.strip()
    if not line:
        return False
        
    return bool(is_topic_prediction(line)[0])