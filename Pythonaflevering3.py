import random
import numpy as np
import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D 

#Vælger en "helt tilfældig" streng som seed:
random.seed(sum([ord(i) for i in 'derborenbager']))


#Først vælger jeg en længde på partiklens 'skridt':
stepsize = 1

#Derefter definerer jeg hvordan den 'går' da jeg får brug for dette flere gange:
def newpos(p,l):
    #Træder et skridt fra p på længden l og returnerer denne  
    r = random.random()*2*np.pi
    return [p[0]+np.cos(r)*l,p[1]+np.sin(r)*l]

#Jeg starter med at partiklen skal tage 5000 skridt derefter 10000 og så 15000 skridt:
steps_per_time = 5000
times_started = 3

#Jeg vælger at lave et for loop da jeg ikke gider sidde og copy paste 5000 gange :(
for ii in range(times_started):
    #Definerer variable
    points = []
    pos = [0,0]
    #Går i gang med appende placeringsvektorerne til en liste
    for i in range(steps_per_time*(1+ii)):
        pos = newpos(pos,stepsize)
        points.append(pos)
    #Starter et nyt plot
    plt.figure(ii)
    
    #Sørger for at titel og akselabels er korrekte
    plt.title("Positioner for partikel efter %s steps"%(steps_per_time*(1+ii)))
    plt.xlabel("x")
    plt.ylabel("y")
    #Laver min liste om til to. Et for x- og et for y-koordinaterne:
    xx, yy = [points[_][0] for _ in range(len(points))],[points[_][1] for _ in range(len(points))]
    #Tegner vejen den er gået:
    plt.scatter(xx,yy)
    #Viser dette
    plt.show()

#Nu vil jeg gerne have at partiklen tager kun 100 skridt. Denne gang skal den gøre dette 20000 gange:
steps_per_time = 100
times_started = 20000

#Jeg laver basalt set samme kode som herover, denne gang gemmer jeg dog kun slutpositionerne
endpoints = []
for ii in range(times_started):
    pos = [0,0]
    for i in range(steps_per_time):
        pos = newpos(pos,stepsize)
    endpoints.append(pos)

#Jeg tegner nu de to plots i samme figur
f, (ax1,ax2) = plt.subplots(1,2)
#Laver to arrays igen. Jeg skulle måske have lavet dette til en funktion.. Eller fundet en indbygget
xx,yy = [endpoints[_][0] for _ in range(len(endpoints))],[endpoints[_][1] for _ in range(len(endpoints))]

#Jeg tegner histogrammerne for x-positionerne
ax1.hist(xx, bins = 500)
ax1.set_xlabel("Slutposition på x-aksen efter 100 steps")
ax1.set_ylabel("Frekvens for slutpositionen")

#Og y-positionerne
ax2.hist(yy,bins = 500)
ax2.set_xlabel("Slutposition på y-aksen efter 100 steps")
ax2.set_ylabel("Frekvens for slutpositionen")
f.suptitle('Frekvens for slutposition på x- og y-aksen')

#Og nu or blær laver jeg et 3D-histogram af dataen herover: 
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(*zip(*points), zs=0, zdir='z', label='curve in (x,y)')
hist, xedges, yedges = np.histogram2d(*zip(*points), bins=100, range=[[-200, 200], [-200, 200]])

# Jeg er nødt til at lave et nyt array med udgangspunkterne for 3d-barerne
xpos, ypos = np.meshgrid(xedges[:-1] + 0.25, yedges[:-1] + 0.25, indexing="ij")
xpos = xpos.ravel()
ypos = ypos.ravel()
zpos = 0
dx = dy = 0.5 * np.ones_like(zpos)
dz = hist.ravel()

#Jeg tegner nu alle de valgte parametre:
ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color='b', zsort='average')

#Og viser denne
plt.show()#You have been Schauser-corrupted!!