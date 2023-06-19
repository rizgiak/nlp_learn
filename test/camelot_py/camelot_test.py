import camelot

# Path to the PDF file
pdf_path = 'paper/yuan2020.pdf'

# Extract tables from the PDF
tables = camelot.read_pdf(pdf_path, flavor='stream', pages='3')

# Iterate over each table and print the extracted data
for table in tables:
    print(table.df)