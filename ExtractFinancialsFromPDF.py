
# 7340 lines in report1.pdf

import os
import re
os.system('cls')

import pdfplumber
"""
def extract_text_from_pdf(pdf_path):
    all_text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            all_text += page.extract_text() + "\n"
    return all_text

def filter_for_word(text, word, num_lines=500):
    lines = text.splitlines()
    total_lines = len(lines)
    
    index = 0
    while index < total_lines:
        line = lines[index]

        if word.lower() in line.lower() and len(line) <= len(word) + 2:
            start = index
            end = min(index + num_lines, total_lines)

            n = 10
            for i in range(1, n+1):
                # block n = 5, i = 1: 1 : 51, i = 2, 51 : 101...
                print(f"\n\nBlock: {(start + ((num_lines)*i)//n - num_lines//n)} to {(end + (((num_lines)*i)//n) - num_lines)}\n\n")
                block = lines[(start + ((num_lines)*i)//n - num_lines//n) - num_lines//n//2 : (end + (((num_lines)*i)//n) - num_lines) + num_lines//n//2]

                #print(f"Found '{word}' in line {index + 1}. Printing lines {start + 1} to {end}:")
                for follow_line in block:
                    count_numbers = sum(len(re.findall(r'\d+', block_line)) for block_line in block)
                    if not count_numbers >= num_lines//n:
                        continue;
                    print(follow_line)
                
            index = end
            print("-" * 40 + "\n" * 3)

        index += 1
"""
pdf_file = "report1.pdf"
#raw_text = extract_text_from_pdf(pdf_file)

#filter(raw_text, 'Income Statement')

import PyPDF2


def filter_for_data(pdf_path):
    total_lines_count = 0

    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text = page.extract_text()
            if not text:
                continue

            for line in text.splitlines():
                line = line.strip()
                if not line:
                    continue

                #words_in_line = 0
                #for i in range(len(line) - 1):
                #    if line[i].isalpha() and line[i+1] == " ":
                #        words_in_line += 1

                #nums_in_line = sum(1 for c in line if c.isdigit())

                #if words_in_line >= 1 and nums_in_line >= 1:
                    #total_lines_count += 1
                    #print(f"words: {words_in_line}, nums: {nums_in_line}")
                print(f'"{line}",')
    
    print(f"Total matching lines: {total_lines_count}")




if __name__ == "__main__":
    pdf_path = "report1.pdf"
    filter_for_data(pdf_path)

    