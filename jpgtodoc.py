import pytesseract

import cv2

import docx

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

image = cv2.imread("image.jpg")

text = pytesseract.image_to_string(image)

doc = docx.Document()

doc.add_paragraph(text)

doc.save("extracted_text.docx")

