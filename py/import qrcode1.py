import qrcode
import PIL
from PIL import Image
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask

qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L)
qr.add_data('Some data')

img_1 = qr.make_image(image_factory=StyledPilImage,
                      module_drawer=RoundedModuleDrawer(),
                      color_mask=RadialGradiantColorMask(),
                      embeded_image_path="rda.png")
img_1.save('qr.png')