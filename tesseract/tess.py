import fitz
import pytesseract
from PIL import Image
from PyPDF2 import PdfFileWriter, PdfFileReader

# Função para converter imagem em PDF em texto editável
def image_to_text(image_path):
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    return text

# Carregue o PDF original
input_pdf = "input.pdf"
pdf_document = fitz.open(input_pdf)

# Inicialize o PDF de saída
output_pdf = PdfFileWriter()

# Loop pelas páginas do PDF original
for page_number in range(pdf_document.page_count):
    page = pdf_document.load_page(page_number)
    
    # Extraia o texto da página
    text = page.get_text("text")
    
    # Extraia as imagens da página
    xobjects = page.get_page_image_list()
    
    for x_object in xobjects:
        xref = x_object[0]
        base_image = pdf_document.extract_image(xref)
        image_data = base_image["image"]

        # Salve a imagem em um arquivo temporário
        image_path = f"temp_image_{page_number}.png"
        with open(image_path, "wb") as f:
            f.write(image_data)

        # Extraia o texto da imagem e anexe ao texto da página
        image_text = image_to_text(image_path)
        text += image_text

    # Crie uma nova página no PDF de saída com o texto extraído
    output_page = fitz.open("pdf").new_page(width=page.width, height=page.height)
    output_page.insert_text(text)
    output_pdf.addPage(output_page)

# Salve o PDF editável
output_pdf_file = "editable_output.pdf"
with open(output_pdf_file, "wb") as f:
    output_pdf.write(f)

print(f"PDF editável gerado: {output_pdf_file}")
