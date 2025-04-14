import csv
import re
import sys

def preprocessor(line):
    key_match = re.match(r'^[A-Za-z ,.]+', line)
    key = key_match.group(0).strip() if key_match else ""
    if not key.strip():
        key = "<EMPTY_KEY>"

    value_match = re.search(r'\(?\d[\d,.\)]*\)?', line)
    value = value_match.group(0) if value_match else "<EMPTY_VALUE>"

    data = f'{key} : {value}'
    return data

def update_training_dataset():
    updated_rows = []
    
    with open("data.csv", newline='', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        
        for row in reader:
            original_input = row["Input"]
            processed_input = preprocessor(original_input)
            if original_input != processed_input:
                print(processed_input)
            row["Input"] = processed_input
            
            updated_rows.append(row)
    
    with open("data.csv", 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(updated_rows)

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "update":
        update_training_dataset()
