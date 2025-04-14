import joblib
import os
from preprocesser import preprocessor

current_dir = os.path.dirname(__file__)
vectorizer = joblib.load(os.path.join(current_dir, 'vectorizer.pkl'))
model = joblib.load(os.path.join(current_dir, 'classifier.pkl'))

def is_financial_data(text):
    text_vector = vectorizer.transform([text])

    prediction = model.predict(text_vector)

    confidence = model.predict_proba(text_vector)[0][prediction[0]]
    return prediction[0] == 1, confidence

if __name__ == '__main__':
    with open("../ExtractFinancialsFromPDF/financials.txt", "r") as file:
        with open("financials.txt", 'w', encoding='utf-8') as txt_file:
            for line in file.readlines():
                line = preprocessor(line)
                line = line.strip()
                if not line:
                    continue
                    
                if is_financial_data(line)[0]:
                    txt_file.write(line + '\n')
