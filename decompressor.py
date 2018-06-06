from PIL import Image
from Image_Class import *
import sys
import pickle

with open('data.txt', 'rb') as fp:
    data = pickle.load(fp)

# print(c.x)
# print(c[0], c[1], c[2], c[3])

d = data.decompress(data.compressed)

m = data.devectorize(d)

import numpy as np

array = np.array(m, dtype=np.uint8)

new_image = Image.fromarray(array)
new_image.save(sys.argv[1])
