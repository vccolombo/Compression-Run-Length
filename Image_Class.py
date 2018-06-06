from PIL import Image

class Image_Class(object):
    def vectorize(self, image):
        v = []
        pix = image.load()
        for x in range(0, self.x):
            for y in range(0, self.y):
                v.extend(pix[x,y])
        return v

    def compress(self, v):
        r = v[0]
        g = v[1]
        b = v[2]
        anterior = [r,g,b]
        counter = 1
        c = []
        for idx in range(3, len(v), 3):
            r = v[idx + 0]
            g = v[idx + 1]
            b = v[idx + 2]
            atual = [r,g,b]
            if(atual == anterior):
                counter = counter + 1
            else:
                # if(counter > 1):
                #     print(counter)
                c.append(counter)
                c.extend(anterior)

                counter = 1
            anterior = atual

        return c


    def __init__(self, image):
        self.x = image.size[0]
        self.y = image.size[1]
        self.vector = self.vectorize(image)
