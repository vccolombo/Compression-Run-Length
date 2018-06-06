from PIL import Image

class Image_Class(object):
    def vectorize(self, image):
        v = []
        pix = image.load()
        for x in range(0, self.x):
            for y in range(0, self.y):
                v.extend(pix[x,y])
        return v

    def __init__(self, image):
        self.x = image.size[0]
        self.y = image.size[1]
        self.vector = self.vectorize(image)
