import csv
import re
from preprocesser import preprocessor

# TODO:
# Extract data from a few lines of unpolished financial data
# Use AI Text Classification to turn determine the category of that data
# Turn it into json

def generate_training_data(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            
            print(f'"{preprocessor(line)}",')
            

if __name__ == '__main__':
    generate_training_data('../ExtractFinancialsFromPDF/financials.txt')
    #pass

