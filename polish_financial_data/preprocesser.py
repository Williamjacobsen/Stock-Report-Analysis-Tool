import re

def preprocessor(line):
    key_match = re.match(r'^[A-Za-z ,.]*', line)
    key = key_match.group(0).strip() if key_match else ""

    # Extract first numeric value
    value_match = re.search(r'\(?\d[\d,.\)]*\)?', line)
    value = value_match.group(0) if value_match else ""

    data = f'{key} : {value}'
    return data