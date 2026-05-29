# Import PdfReader class from PyPDF2
from PyPDF2 import PdfReader


# Function to extract text from uploaded PDF
def extract_text(pdf_file):

    # Empty variable to store all text
    text = ""

    # Open and read PDF file
    reader = PdfReader(pdf_file)

    # Loop through each page in PDF
    for page in reader.pages:

        # Extract text from page
        # Add it to text variable
        text += page.extract_text()

    # Return complete extracted text
    return text