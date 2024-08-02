import qrcode
from PIL import Image, ImageDraw
from qrcode.image.styles.colormasks import SolidFillColorMask
from qrcode.image.styledpil import StyledPilImage, SolidFillColorMask
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask


qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L)
qr.add_data('Some data')

qr_eyes_img = qr.make_image(image_factory=StyledPilImage,
                            eye_drawer=RoundedModuleDrawer(radius_ratio=1.2),
                            color_mask=SolidFillColorMask(back_color=(255, 255, 255), front_color=(255, 110, 0)))

qr_img = qr.make_image(image_factory=StyledPilImage,
                      color_mask=RadialGradiantColorMask(),
                      module_drawer=RoundedModuleDrawer(),
                      embeded_image_path="rda.png")


qr_img.save('qrcode.png')


