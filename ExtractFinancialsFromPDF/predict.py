import joblib
import re

def preprocess(text):
    text = re.sub(r'\d+[\.,]?\d*', '<NUM>', text)
    return text.lower()

vectorizer = joblib.load('vectorizer.pkl')
model = joblib.load('classifier.pkl')

def classify_text(text):
    processed = preprocess(text)

    text_vector = vectorizer.transform([processed])

    prediction = model.predict(text_vector)

    confidence = model.predict_proba(text_vector)[0][prediction[0]]
    return "Numerical Data" if prediction[0] == 1 else "Narrative Text", confidence

test_cases = [
    ["Intangible assets 6 19,449 9,110", "Numerical Data"],
    ["Interest income relating to subsidiaries 365 238", "Numerical Data"],
    ["Financial gain from forward contracts (net) — 2,021", "Numerical Data"],
    ["Other financial income 202 156", "Numerical Data"],
    ["Total financial income 567 2,415", "Numerical Data"],
    ["Interest expenses relating to subsidiaries 1,150 13", "Numerical Data"],
    ["Result of associated company 4 13", "Numerical Data"],
    ["Foreign exchange loss (net) 2,705 1,978", "Numerical Data"],
    ["Financial loss from forward contracts (net) 1,659 —", "Numerical Data"],
    ["Capital loss from marketable securities 463 44", "Numerical Data"],
    ["Other financial expenses 299 177", "Numerical Data"],
    ["Total financial expenses 6,280 2,225DKK million 2022 2021", "Numerical Data"],
    ["Diabetes and Obesity care 142,413 112,347", "Numerical Data"],
    ["Rare disease 243 206", "Numerical Data"],
    ["Total sales 142,656 112,553", "Numerical Data"],
    ["North America Operations 79,953 57,654", "Numerical Data"],
    ["EMEA 32,789 27,124", "Numerical Data"],
    ["China 14,412 15,608", "Numerical Data"],
    ["Rest of World 15,502 12,167", "Numerical Data"],
    ["Total sales 142,656 112,553", "Numerical Data"],
    ["The net profit of subsidiaries and associated companies less unrealised","Narrative Text"],
    ["intra-group profits and amortisation of goodwill is recorded in the income","Narrative Text"],
    ["statement of the parent company. To the extent that net profit exceeds","Narrative Text"],
    ["declared dividends from such companies, the net revaluation of investments","Narrative Text"],
    ["in subsidiaries and associated companies is transferred to net revaluation","Narrative Text"],
    ["reserve under equity according to the equity method. Profits in subsidiaries","Narrative Text"],
    ["and associated companies are disclosed as profit after tax.","Narrative Text"],
    ["Amounts owed by affiliates, where settlement is neither planned nor likely","Narrative Text"],
    ["within the foreseeable future, are treated as part of net-investments in","Narrative Text"],
    ["subsidiaries, with exchange rate adjustments recognised directly in equity","Narrative Text"],
    ["through reserve for cash flow hedges and exchange rate adjustments. Tax","Narrative Text"],
    ["For Danish tax purposes, the parent company is assessed jointly with its","Narrative Text"],
    ["Danish subsidiaries. The Danish jointly taxed companies are included in a","Narrative Text"],
    ["Danish on-account tax payment scheme for Danish corporate income tax.","Narrative Text"],
    ["All current taxes under the scheme are recorded in the individual companies.","Narrative Text"],
    ["Novo Nordisk A/S and its jointly taxed subsidiaries are included in the joint","Narrative Text"],
]

correct_guesses = 0
guesses = 0

for case in test_cases:
    result, confidence = classify_text(case[0])

    guesses += 1
    if result == case[1]:
        correct_guesses += 1

    print(result == case[1])
    print(f"result: {result}, confidence: {confidence}, text: {case[0]}, answer: {case[1]}")

accuracy = correct_guesses/guesses
print(f"Accuracy: {accuracy*100}%")

# Without any preprocessing
# 70% accuracy

# With preprocessing <NUM>
# 94% accuracy