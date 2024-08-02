import qrcode


from PIL import Image


def generate_custom_qrcode(data, logo_path):


  qr = qrcode.QRCode(


  version=1,


  error_correction=qrcode.constants.ERROR_CORRECT_H,


  box_size=10,


  border=4,


)


# Exemplo de uso:


data = "https://www.example.com"

logo_path = "rda.png"

qr = qrcode.QRCode()

qr.add_data(data)

qr.make(fit=True)

logo = Image.open(logo_path)

qr_img = qr.make_image(fill_color="black", back_color="white")

logo_size = qr_img.size[0] // 4


logo_resized = logo.resize((logo_size, logo_size))


qr_img.paste(logo_resized, (qr_img.size[0] // 2 - logo_resized.size[0] // 2, qr_img.size[1] // 2 - logo_resized.size[1] // 2))


qr_img.show()

qr_img = generate_custom_qrcode(data, logo_path)

qr_img.save('test.png')