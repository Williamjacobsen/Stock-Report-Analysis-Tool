import re

def preprocess(text):
    text = re.sub(r'\d{4}', '<DATE>', text)
    text = re.sub(r'\d+[\.,]?\d*', '<NUM>', text)
    text = re.sub(r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*', '<DATE>', text)
    text = re.sub(r'(<NUM>/<NUM>|<DATE>/<NUM>)', '<DATE>', text)
    return text.lower()

s = """Delaware 94-3177549
Registrant’s telephone number, including area code: (408) 486-2000
October 28, 2024 - November 24, 2024 25.4 $ 142.67 25.4 $ 42.8
November 25, 2024 - December 22, 2024 10.6 $ 136.86 10.6 $ 41.4
December 23, 2024 - January 26, 2025 19.3 $ 139.30 19.3 $ 38.7
Total 55.3 55.3
NVIDIA  Corporation $ 100.00 $ 207.79 $ 365.66 $ 326.34 $ 978.42 $ 2,287.06
S&P 500 $ 100.00 $ 114.79 $ 138.90 $ 129.69 $ 158.39 $ 200.32
Nasdaq 100 $ 100.00 $ 142.64 $ 160.62 $ 136.37 $ 196.94 $ 248.12
Revenue $ 130,497 $ 60,922 Up 114%
January 26, 2025; 24,643 shares issued and outstanding as of January 28, 2024 24 25"""

print(preprocess(s))