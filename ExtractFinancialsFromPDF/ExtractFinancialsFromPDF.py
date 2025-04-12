import PyPDF2
from predict import classify_text

def ExtractFinancialsFromPDF(pdf_path):
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

                if classify_text(line)[0] == "Numerical Data":
                    print(line)

if __name__ == "__main__":
    import os
    os.system('cls')

    pdf_path = "../msft2021.pdf"
    ExtractFinancialsFromPDF(pdf_path)