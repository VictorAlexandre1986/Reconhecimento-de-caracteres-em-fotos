from pytesseract import pytesseract
from PIL import Image
import os

#Não é necessário usar essa biblioteca
img = Image.open('imagem2.jpg')

# pytesseract.tesseract_cmd=r'C:\tesseract\tesseract.exe'
pytesseract.tesseract_cmd = os.path.join("C:\\tesseract","tesseract.exe")

#duas maneiras que pode ser feito, mas o primeiro tem que usar a biblioteca PIL
#text = pytesseract.image_to_string(img)
text = pytesseract.image_to_string(f'imagem3.jpg')

linhas = text.split('\n')

print(linhas)

print(''.join(linhas))