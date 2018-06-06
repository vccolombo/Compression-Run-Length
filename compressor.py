from PIL import Image
from Image_Class import *
import sys

image = Image_Class(Image.open(sys.argv[1]))

r = image.vector[0]
g = image.vector[1]
b = image.vector[2]
anterior = [r,g,b]
counter = 1
v = []
for idx in range(3, len(image.vector), 3):
    r = image.vector[idx + 0]
    g = image.vector[idx + 1]
    b = image.vector[idx + 2]
    atual = [r,g,b]
    if(atual == anterior):
        counter = counter + 1
    else:
        # if(counter > 1):
        #     print(counter)
        v.append(counter)
        v.extend(anterior)

        counter = 1
    anterior = atual

# print(len(v))
# print(len(image.vector))
