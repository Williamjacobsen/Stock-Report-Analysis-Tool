import PyPDF2
from predict import classify_text

def ExtractFinancialsFromPDF(pdf_path, output_txt_path):  # This reduced the report size by 80%
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        with open(output_txt_path, 'w', encoding='utf-8') as txt_file:
            for page in reader.pages:
                text = page.extract_text()
                if not text:
                    continue

                for line in text.splitlines():
                    line = line.strip()
                    if not line:
                        continue
                    
                    if classify_text(line)[0] == "Numerical Data":
                        txt_file.write(line + '\n')

if __name__ == "__main__":
    import os
    os.system('cls')

    pdf_path = "../msft2021.pdf"
    output_txt_path = "financials_output_unpolished.txt"
    ExtractFinancialsFromPDF(pdf_path, output_txt_path)