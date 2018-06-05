from PIL import Image
from Image_Class import *
import sys

image = Image.open(sys.argv[1])
pix = image.load()
print(image.size)

image2 = Image_Class(image)
