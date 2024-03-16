import fitz  # PyMuPDF
import PyPDF2
import pdfplumber

def extract_text_with_pymupdf(pdf_path):
    text = ""
    doc = fitz.open(pdf_path)
    for page_num in range(doc.page_count):
        page = doc[page_num]
        text += page.get_text()
    return text

def extract_text_with_pypdf2(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    return text

def extract_links_images_tables_with_pdfplumber(pdf_path):
    links = []
    images = []
    tables = []
    with pdfplumber.open(pdf_path) as pdf:
        for page_num in range(len(pdf.pages)):
            page = pdf.pages[page_num]
            
            # Extract links
            links.extend(link["url"] for link in page.links)
            
            # Extract images
            images.extend(image["src"] for image in page.images)
            
            # Extract tables
            tables.extend(table.extract() for table in page.extract_tables())
    
    return links, images, tables

# Replace 'your_pdf_path.pdf' with the actual path to your PDF file
pdf_path = 'F:\Catalog Digitization\sofa-catalog.pdf'

# Extract text using PyMuPDF
text_pymupdf = extract_text_with_pymupdf(pdf_path)
print("Text (PyMuPDF):", text_pymupdf)

# Extract text using PyPDF2
text_pypdf2 = extract_text_with_pypdf2(pdf_path)
print("Text (PyPDF2):", text_pypdf2)

# Extract links, images, and tables using PdfPlumber
links, images, tables = extract_links_images_tables_with_pdfplumber(pdf_path)
#         print("Links:", links)
print("Images:", images)
print("Tables:", tables)
