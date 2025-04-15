import sys
import os
import json

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from polish_financial_data.preprocesser import get_key, get_value

def save_fincials_to_json():
    data = {}

    with open("../financials.txt", "r") as input_file:
        for line in input_file.readlines():
            data[get_key(line)] = get_value(line)

    with open("financial_data.json", "w") as json_file:
        json.dump(data, json_file, indent=4)

def get_context_of_data(line):
    pass

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "save":
        save_fincials_to_json()
