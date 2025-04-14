from is_financial_data import is_financial_data

test_cases = [
    ["Intangible assets 6 19,449 9,110", 1],
    ["Interest income relating to subsidiaries 365 238", 1],
    ["Financial gain from forward contracts (net) — 2,021", 1],
    ["Other financial income 202 156", 1],
    ["Total financial income 567 2,415", 1],
    ["Interest expenses relating to subsidiaries 1,150 13", 1],
    ["Result of associated company 4 13", 1],
    ["Foreign exchange loss (net) 2,705 1,978", 1],
    ["Financial loss from forward contracts (net) 1,659 —", 1],
    ["Capital loss from marketable securities 463 44", 1],
    ["Other financial expenses 299 177", 1],
    ["Total financial expenses 6,280 2,225DKK million 2022 2021", 1],
    ["Diabetes and Obesity care 142,413 112,347", 1],
    ["Rare disease 243 206", 1],
    ["Total sales 142,656 112,553", 1],
    ["North America Operations 79,953 57,654", 1],
    ["EMEA 32,789 27,124", 1],
    ["China 14,412 15,608", 1],
    ["Rest of World 15,502 12,167", 1],
    ["Total sales 142,656 112,553", 1],
    ["The net profit of subsidiaries and associated companies less unrealised", 0],
    ["intra-group profits and amortisation of goodwill is recorded in the income", 0],
    ["statement of the parent company. To the extent that net profit exceeds", 0],
    ["declared dividends from such companies, the net revaluation of investments", 0],
    ["in subsidiaries and associated companies is transferred to net revaluation", 0],
    ["reserve under equity according to the equity method. Profits in subsidiaries", 0],
    ["and associated companies are disclosed as profit after tax.", 0],
    ["Amounts owed by affiliates, where settlement is neither planned nor likely", 0],
    ["within the foreseeable future, are treated as part of net-investments in", 0],
    ["subsidiaries, with exchange rate adjustments recognised directly in equity", 0],
    ["through reserve for cash flow hedges and exchange rate adjustments. Tax", 0],
    ["For Danish tax purposes, the parent company is assessed jointly with its", 0],
    ["Danish subsidiaries. The Danish jointly taxed companies are included in a", 0],
    ["Danish on-account tax payment scheme for Danish corporate income tax.", 0],
    ["All current taxes under the scheme are recorded in the individual companies.", 0],
    ["Novo Nordisk A/S and its jointly taxed subsidiaries are included in the joint", 0],
]

correct_guesses = 0
guesses = 0

for case in test_cases:
    result, confidence = is_financial_data(case[0])

    guesses += 1
    if result == case[1]:
        correct_guesses += 1

    print(f"correct?: {result==case[1]}, result: {result}, confidence: {confidence}, text: {case[0]}, answer: {case[1]}")

accuracy = correct_guesses/guesses
print(f"Accuracy: {accuracy*100}%")