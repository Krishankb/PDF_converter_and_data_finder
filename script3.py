import pdfplumber

def email_selector():
    pdf_file_na= "Converted\doc2pdfconverted.pdf"
    pdf = pdfplumber.open(pdf_file_na) 
    page = pdf.pages[0]
    text = page.extract_text()
    for row in text.split('\n'):
        if row.startswith('Email'):
            email = row.split()[-1]
            return email

def mobile_selector():
    pdf_file_na= "Converted\doc2pdfconverted.pdf"
    with pdfplumber.open(pdf_file_na) as pdf:
        page= pdf.pages[0]
        text = page.extract_text()
        for row in text.split('\n'):
            if row.startswith('Mobile'):
                mobile = row.split()
                return mobile
            elif row.startswith('Contact'):
                mobile = row.split()
                return mobile
