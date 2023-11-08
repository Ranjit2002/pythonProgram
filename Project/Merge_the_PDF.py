"""
1. Write a program to manipulate PDF files using pyPDF. Your program should be able to merge
   multiple PDF files into a single PDF. You are welcome to add more functionalities

2. pyPDF is a free and open-source pure python PDF library capable of splitting, merging, cropping
   and transforming the pages of PDF files. It can also add custom data, viewing options and passwords
   to PDF files. pyPDF can retrieve text and metadata from PDFs as well.
"""

import PyPDF2

# Create a PDF merger object
pdf_merger = PyPDF2.PdfFileMerger()

# Add the PDF files you want to merge
pdf_merger.append('file1.pdf')
pdf_merger.append('file2.pdf')
pdf_merger.append('file3.pdf')

# Output file where the merged PDF will be saved
output_pdf = open('merged.pdf', 'wb')

# Write the merged PDF to the output file
pdf_merger.write(output_pdf)

# Close the input and output files
pdf_merger.close()
output_pdf.close()
