import sys
import PyPDF2
import os

clean_file = PyPDF2.PdfFileReader(open(f'{sys.argv[1]}', 'rb'))
watermark = PyPDF2.PdfFileReader(open(f'{sys.argv[2]}', 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(clean_file.getNumPages()):
    page = clean_file.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

    with open('watered.pdf', 'wb') as file:
        output.write(file)

