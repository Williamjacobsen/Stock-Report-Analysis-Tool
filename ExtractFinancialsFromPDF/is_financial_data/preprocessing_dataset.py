import re
import pandas as pd

def replace_numbers(text):
    if pd.isna(text):
        return text
    text = re.sub(r'\d{4}', '<DATE>', text)
    text = re.sub(r'\d+[\.,]?\d*', '<NUM>', text)
    text = re.sub(r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*', '<DATE>', text)
    text = re.sub(r'(<NUM>/<NUM>|<DATE>/<NUM>)', '<DATE>', text)
    return text

input_file = "../data.csv"
output_file = "preprocessed_data.csv"

data = pd.read_csv(input_file)

data['financial_data'] = data['financial_data'].apply(replace_numbers)

data.to_csv(output_file, index=False)
