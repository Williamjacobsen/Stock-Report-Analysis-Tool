import PyPDF2
from is_financial_data.is_financial_data import is_financial_data
from polish_financial_data.main import is_polished_financial_data
from polish_financial_data.preprocesser import preprocessor
from get_topic.main import is_topic

def ExtractFinancialsFromPDF(pdf_path, output_txt_path):
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        with open(output_txt_path, 'w', encoding='utf-8') as txt_file:

            topic = ""

            for page in reader.pages:
                text = page.extract_text()
                if not text:
                    continue

                for line in text.splitlines():
                    line = line.strip()
                    if not line:
                        continue

                    if is_topic(line):
                        print(line)
                    
                    if is_financial_data(line)[0] and is_polished_financial_data(line):
                        txt_file.write(preprocessor(line) + '\n')

if __name__ == "__main__":
    import os
    os.system('cls')

    pdf_path = "../reports/pcar2023.pdf"
    output_txt_path = "financials.txt"
    ExtractFinancialsFromPDF(pdf_path, output_txt_path)
