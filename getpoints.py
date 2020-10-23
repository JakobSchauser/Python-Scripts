from PIL import Image
from scipy import optimize

threshold = 500
quality = 1
img = Image.open("graph.png")
pix = img.load()

points = []
sz = img.size

for w in range(0,sz[0],quality):
    for h in range(0,sz[1],quality):
        if(sum(pix[w,h]) < threshold):
            pix[w,h] = (255,0,0,0)
            points.append([w,sz[1]-h])
            break

            
img.show()