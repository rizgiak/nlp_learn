import tabula

# Path to the PDF file
pdf_path = 'paper/yuan2020.pdf'

# Extract tables from the PDF
tables = tabula.read_pdf(pdf_path, pages="all")

print(len(tables))

# Iterate over each table and print the extracted data
i = 0
for table in tables:
    print("Table " + str(i))
    table.to_csv('csv/output' + str(i) + '.csv', encoding='utf-8')
    print(table)
    print("\n\n")
    i += 1
