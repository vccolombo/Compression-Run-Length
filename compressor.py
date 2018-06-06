from PIL import Image
from Image_Class import *
import sys
import pickle

image = Image_Class(Image.open(sys.argv[1]))

with open("data.txt", 'wb') as fp:
    pickle.dump(image, fp)
