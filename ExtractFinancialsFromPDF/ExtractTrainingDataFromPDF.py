import PyPDF2

def ExtractTraningDataFromPDF(pdf_path):
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

                print(f'"{line}",')

if __name__ == "__main__":
    import os
    os.system('cls')

    pdf_path = "../aapl2023.pdf"
    ExtractTraningDataFromPDF(pdf_path)