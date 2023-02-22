#!/usr/bin/python3

import os
from PyPDF2 import PdfFileMerger

# Directory containing PDF files to merge
dir_path = os.path.join(os.path.expanduser('~'), 'work/pdf_files')

# Create a PdfFileMerger object
merger = PdfFileMerger()

# Loop through all PDF files in the directory
for filename in os.listdir(dir_path):
    if filename.endswith('.pdf'):
        filepath = os.path.join(dir_path, filename)
        # Add the PDF file to the merger object
        merger.append(filepath)

# Write the merged PDF to a file
output_file = os.path.join(dir_path, 'merged.pdf')
merger.write(output_file)

# Close the merger object
merger.close()
