import csv
import re
import pandas as pd

def replace_numbers(text):
    if pd.isna(text):
        return text
    return re.sub(r'\d+[\.,]?\d*', '<NUM>', text)

input_file = "data.csv"
output_file = "preprocessed_data.csv"

data = pd.read_csv(input_file)

data['text'] = data['text'].apply(replace_numbers)

data.to_csv(output_file, index=False)
