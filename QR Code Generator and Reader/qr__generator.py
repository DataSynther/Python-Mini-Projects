# In this part we will learn how to create a QR code generator using Python.

import pyqrcode
import png
link = "https://inventwithpython.com/bigbookpython/project1.html"
qr_code = pyqrcode.create(link)
qr_code.png("instagram.png", scale=5)

