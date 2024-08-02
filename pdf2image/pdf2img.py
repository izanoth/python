from pdf2image import convert_from_path


# Store Pdf with convert_from_path function
pages = convert_from_path('hct.pdf', 500, first_page=30, last_page=46, poppler_path=r"C:\Arquivos de Programas\poppler-21.08.0\Library\bin")

for count, page in enumerate(pages):
#    print(count)
    page.save(f'hct/hct{count}.jpg', 'JPEG')

#for i in range(len(images)):
#   images[i].save('page'+ str(i) +'.jpg', 'JPEG')