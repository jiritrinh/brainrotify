import os
import pymupdf 
 


def extract_text(pdf_filename):
    BASE_DIR = os.path.dirname(__file__)
    pdf_path = os.path.join(BASE_DIR, "pdfs", pdf_filename)
    doc = pymupdf.open(pdf_path)  
    extracted_text = ""
    for page in doc:  
        extracted_text += page.get_text() + "\n"  
    return extracted_text





