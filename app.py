from pytesseract import pytesseract
from PIL import Image
import os

img = Image.open('imagem2.jpg')

# pytesseract.tesseract_cmd=r'C:\tesseract\tesseract.exe'
pytesseract.tesseract_cmd = os.path.join("C:\\tesseract","tesseract.exe")


text = pytesseract.image_to_string(f'imagem3.jpg')

linhas = text.split('\n')

print(linhas)

print(''.join(linhas))