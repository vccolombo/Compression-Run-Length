from PIL import Image
from Image_Class import *
import sys
import pickle

image = Image_Class(Image.open(sys.argv[1]))

c = image.compress(image.vector)

with open('test.txt', 'wb') as fp:
    pickle.dump(c, fp)

# print(c[0], c[1], c[2], c[3])
