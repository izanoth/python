import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask
from PIL import Image, ImageDraw



def style_eyes(img, hg):
  img_size = img.size[0]
  eye_size = 70 #default
  quiet_zone = 40 #default
  draw = ImageDraw.Draw(mask)
  draw.rectangle((40, 40, 110, 110), fill=255)
  draw.rectangle((img_size-110, 40, img_size-40, 110), fill=255)
  draw.rectangle((40, img_size-110, 110, img_size-40), fill=255)
  return mask


qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L)
qr.add_data('Some data')

qrcd = qr.make_image(image_factory=StyledPilImage, 
                      module_drawer=RoundedModuleDrawer(), 
                      color_mask=RadialGradiantColorMask(), 
                      embeded_image_path="rda.png")


logo = Image.open('rda.png')
 # taking base width
basewidth = 100
# adjust image size
wpercent = (basewidth/float(logo.size[0]))
hsize = int((float(logo.size[1])*float(wpercent)))
logo = logo.resize((basewidth, hsize))
# set size of QR code
wd = ((qrcd.size[0] - logo.size[0]) // 2, (qrcd.size[1] - logo.size[1]) // 2)

mask = style_eyes(qrcd, wd)
#final_img = Image.composite(qr_eyes_img, qr_img, mask)
print(mask)
mask.show()
#print(mask)
#dir(mask)






