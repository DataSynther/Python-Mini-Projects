## Using this script we will learn how to read a PDF file and extract text from it.

from PyPDF2 import PdfReader

reader = PdfReader("SQL cheatsheet.pdf")
text = ""
for page in reader.pages:
    text += page.extract_text() + "\n"
print(text)