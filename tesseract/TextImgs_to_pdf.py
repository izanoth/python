from PIL import Image
import pytesseract
from pytesseract import Output
from fpdf import FPDF
from os import listdir
from os.path import isfile, join

# Lista de caminhos para as imagens que você deseja converter
imgs = []
file = [f for f in listdir('.') if isfile(join('.', f))]
for i in file:
    if i.endswith('.png'):
        imgs.append(i)
    else:
        continue

# Loading Tesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# Inicialize o objeto PDF
pdf = FPDF()

# Defina o formato da página (padrão é 'A4')
pdf.add_page()

# Defina a fonte e o tamanho
pdf.set_font("Arial", size=12)

for image_path in imgs:
    # Abra a imagem usando o PIL (Pillow)
    img = Image.open(image_path)

    # Use o Tesseract para extrair o texto da imagem
    text = pytesseract.image_to_string(img, output_type=Output.STRING)

    # Adicione o texto ao PDF
    pdf.multi_cell(0, 10, text.encode("utf-8").decode("latin-1"))
    pdf.ln()

# Salve o PDF em um arquivo
pdf.output("output.pdf")




