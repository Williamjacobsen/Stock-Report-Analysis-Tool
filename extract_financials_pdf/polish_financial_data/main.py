import joblib
import os
from .preprocesser import preprocessor


current_dir = os.path.dirname(__file__)
vectorizer = joblib.load(os.path.join(current_dir, 'vectorizer.pkl'))
model = joblib.load(os.path.join(current_dir, 'classifier.pkl'))

def is_clean_financial_data(text):
    """This model is trained on the mistakes made by the is_financial_data package"""
    text_vector = vectorizer.transform([text])

    prediction = model.predict(text_vector)

    confidence = model.predict_proba(text_vector)[0][prediction[0]]
    return prediction[0] == 1, confidence

def polish_financial_data_file():
    with open("../financials_unpolished.txt", "r") as file:
        with open("../financials_polished.txt", 'w', encoding='utf-8') as txt_file:
            for line in file.readlines():
                line = preprocessor(line)
                line = line.strip()
                if not line:
                    continue
                    
                if is_clean_financial_data(line)[0]:
                    txt_file.write(line + '\n')

def is_polished_financial_data(line):
    line = preprocessor(line)
    line = line.strip()
    if not line:
        return False
        
    return bool(is_clean_financial_data(line)[0])