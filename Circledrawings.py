from PIL import Image
import math

num = 20

img = Image.open("")
pix = img.load()
sz = img.size
res = [math.floor(_/num) for _ in sz]

def getavg():
    pass

for i in range(res[0]):
    for ii in range(res[1]):
        pix[]