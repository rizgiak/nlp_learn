import fitz

my_path = "my_pdf_file.pdf"
doc = fitz.open(my_path)

for page in doc:
    text = page.get_text()
    print(text)

output = page.get_text("blocks")