import csv
import re

# TODO:
# Extract data from a few lines of unpolished financial data
# Use AI Text Classification to turn determine the category of that data
# Turn it into json

def generate_training_data(input_file_path, output_file_path):
    with open(input_file_path, 'r') as infile, open(output_file_path, mode='w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(['Input', 'Class'])  # Write header

        for line in infile:
            line = line.strip()
            if not line:
                continue

            # Extract key (letters and spaces from start of line)
            key_match = re.match(r'^[A-Za-z ,.]*', line)
            key = key_match.group(0).strip() if key_match else ""

            # Extract first numeric value
            value_match = re.search(r'\(?\d[\d,.\)]*\)?', line)
            value = value_match.group(0) if value_match else ""

            row = f'{key} : {value}'
            writer.writerow([row, ''])

# Example usage:
generate_training_data('../ExtractFinancialsFromPDF/financials.txt', 'output.csv')

