from PIL import Image

class Image_Class(object):
    def vectorize(self, image):
        v = []
        pix = image.load()
        for x in range(0, self.x):
            for y in range(0, self.y):
                v.extend(pix[x,y])
        return v


    def devectorize(self, v):
        matrix = []
        r = []
        for x in range(0, len(v), 3):
            if(x % (self.y*3) == 0 and x != 0):
                matrix.append(r)
                r = []

            r.append((v[x], v[x+1], v[x+2]))


        return matrix


    def decompress(self, v):
        d = []
        for idx in range(0, len(v), 4):
            n = v[idx+0]
            r = v[idx+1]
            g = v[idx+2]
            b = v[idx+3]
            rgb = [r,g,b]
            for times in range(0, n):
                d.extend(rgb)
        return d


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
                c.append(counter)
                c.extend(anterior)
                counter = 1
            anterior = atual

        c.append(counter)
        c.extend(anterior)
        return c


    def __init__(self, image):
        self.x = image.size[0]
        self.y = image.size[1]
        self.vector = self.vectorize(image)
        self.compressed = self.compress(self.vector)
