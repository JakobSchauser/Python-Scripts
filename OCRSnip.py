import numpy as np
from PIL.ImageGrab import grabclipboard
from pytesseract import image_to_string as ocr
from numpy import array
import pyperclip
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

im = grabclipboard()

if im:
    t = ocr(array(im))
    print(t)
    pyperclip.paste(t)
else:
    print("No image was found")

input("")