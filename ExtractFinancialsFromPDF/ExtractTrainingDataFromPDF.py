import PyPDF2

def ExtractTraningDataFromPDF(pdf_path):
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

                print(f'"{line}",')
    
    print(f"Total matching lines: {total_lines_count}")

if __name__ == "__main__":
    import os
    os.system('cls')

    pdf_path = "../report2.pdf"
    ExtractTraningDataFromPDF(pdf_path)