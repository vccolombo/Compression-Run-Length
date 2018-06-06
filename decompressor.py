from PIL import Image
from Image_Class import *
import sys
import pickle

with open('test.txt', 'rb') as fp:
    c = pickle.load(fp)

# print(c.x)
# print(c[0], c[1], c[2], c[3])

d = Image_Class.decompress(c.compressed)

print(len(d))
