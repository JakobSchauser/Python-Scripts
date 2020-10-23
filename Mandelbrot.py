import PIL
import numpy as np
import time

resolution = 10
xsize = 2.5
ysize = 3
maxdepth = 255

img = PIL.Image.new('RGBA',(int(xsize*resolution),int(ysize*resolution)))
data = np.zeros((int(xsize*resolution),int(ysize*resolution),4),dtype = 'int')
#data += 224
def s_range(mi,ma,s):
    return [_/s for _ in range(int(mi*s),int(ma*s))]
    
def check_points():
    for r in range(int(resolution*xsize)):
        for i in range(int(resolution*ysize)):
            pos = [r/resolution-xsize/2,i/resolution-ysize/2]
            val = mandel(pos,pos)
            data[r,i] = [val,val,val,val]
            img.putpixel((r,i),(val,val,val))
            
        way = 100*r/(resolution*xsize)
        if(way % 5 == 0):
            print(way, "%")




    
def mandel(Z,Z0,n = 0):
    n_Z = [Z[0]**2-Z[1]**2+Z0[0] , 2*Z[0]*Z[1]+Z0[1]]
    if(n>=maxdepth) or (n_Z[0]**2 + n_Z[1]**2 > 4):
        return n
    return mandel(n_Z,Z0,n+1)
    
def draw(data):
    im = PIL.Image.fromarray(data,'RGB')
    im.show()
    #im.save('imagetest.png')




starttime = np.floor(time.time())
print("Calculating..")
check_points()
print("Drawing..")
#draw(data)
img.show()
print("Done!")
timetook = np.floor(time.time()) - starttime
print("This calculation took " + str(timetook) + " seconds!" )

    #You have been Schauser-corrupted!!