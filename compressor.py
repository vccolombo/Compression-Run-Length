from PIL import Image
from Image_Class import *
import sys
import pickle

image = Image_Class(Image.open(sys.argv[1]))

with open('test.txt', 'wb') as fp:
    pickle.dump(image, fp)

with open('test_c.txt', 'wb') as fp:
    pickle.dump(image.compressed, fp)

with open('test_o.txt', 'wb') as fp:
    pickle.dump(image.vector, fp)
