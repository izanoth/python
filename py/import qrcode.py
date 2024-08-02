import PIL
from PIL import Image, ImageDraw
from qrcode.image.styles.colormasks import SolidFillColorMask
from qrcode.image.styledpil import StyledPilImage, SolidFillColorMask
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer, VerticalBarsDrawer, SquareModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask

def style_inner_eyes(img):
    img_size = img.size[0]
    eye_size = 70
    quiet_zone = 40
    mask = Image.new('L', img_size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rectangle((60, 60, 90, 90), fill=255)
    draw.rectangle((abs(img_size-90), 60, abs(img_size-60), 90), fill=255)
    draw.rectangle((60, abs(img_size-90), 90, abs(img_size-60)), fill=255)
    return mask

def style_outer_eyes(img):
    img_size = img.size[0]
    eye_size = 70
    quiet_zone = 40
    mask = Image.new('L', img_size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rectangle((40, 40, 110, 110), fill=255)
    draw.rectangle((abs(img_size-110), 40, abs(img_size-40), 110), fill=255)
    draw.rectangle((40, abs(img_size-110), 110, abs(img_size-40)), fill=255)
    draw.rectangle((60, 60, 90, 90), fill=0)
    draw.rectangle((abs(img_size-90), 60, abs(img_size-60), 90), fill=0)
    draw.rectangle((60, abs(img_size-90), 90, abs(img_size-60)), fill=0)
    return mask

if not hasattr(PIL.Image, 'Resampling'):
    PIL.Image.Resampling = PIL.Image

qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
qr.add_data('Some data')

qr_inner_eyes_img = qr.make_image(image_factory=StyledPilImage, 
                                  eye_drawer=RoundedModuleDrawer(radius_ratio=1.2),
                                  color_mask=SolidFillColorMask(back_color=(255,255,255), front_color=(63,42,86)))

qr_outer_eyes_img = qr.make_image(image_factory=StyledPilImage,
                                  eye_drawer=VerticalBarsDrawer(),
                                  color_mask=SolidFillColorMask(front_color=(255,128,0)))

qr_img = qr.make_image(image_factory=StyledPilImage,
                       module_drawer = SquareModuleDrawer(),
                       embeded_image_path="rda.png")

inner_eye_mask = style_inner_eyes(qr_img)
outer_eye_mask = style_outer_eyes(qr_img)
intermediate_img = Image.composite(qr_inner_eyes_img, qr_img, inner_eye_mask)
final_img = Image.composite(qr_outer_eyes_img, intermediate_img, outer_eye_mask)
final_img.save('qrcode.png')
