from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument

fp = open('yuan2020.pdf', 'rb')
parser = PDFParser(fp)
doc = PDFDocument(parser)

print(doc.info)  # The "Info" metadata