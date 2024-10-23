import os
from PyPDF2 import PdfReader, PdfWriter

def split_pdf(input_pdf, output_dir):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Open the PDF file
    reader = PdfReader(input_pdf)
    
    # Split each page into a separate PDF
    for page_num in range(len(reader.pages)):
        writer = PdfWriter()
        writer.add_page(reader.pages[page_num])
        
        # Create a file for each page
        output_filename = f"{output_dir}/page_{page_num + 1}.pdf"
        with open(output_filename, "wb") as output_pdf:
            writer.write(output_pdf)
        
        print(f"Created: {output_filename}")


