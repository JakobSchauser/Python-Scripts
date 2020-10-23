#Jeg starter med at importere en masse ting
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
import math

#Dette er lysets hastighed i vakuum
c = 299792458

#Jeg bruger det opgivne data som jeg importerer således
data = np.genfromtxt('dataLys.csv',delimiter='\t',skip_header = 1)

#Jeg finder længderne, jeg kan se er første kolonne
længder = data[]

#Jeg finder længderne fra datasættet
tid = [data[i,1:] for i in range(len(data))]
    
#Jeg beregner deres gennemsnit og standardafvigelse.
#(Skriv bare hvis I vil have mere forståelig kode)
gns_tid = [sum(t)/len(t) for t in tid]
std_tid = [np.std(t,ddof=1)/np.sqrt(len(t))*5 for t in tid]

#Jeg definerer det linære fit jeg kunne tænke mig at lave.
def fitLin(x,a,b):
    return a*x+b

#Jeg lader herefter SciPy work its magic:
val, cov = optimize.curve_fit(fitLin,længder,gns_tid)

#Jeg startet et plot ved at indtegne de beregnede gennemsnit
plt.plot(længder,gns_tid,'.',label = 'Data')

#Jeg indtegner også vores fit
plt.plot(længder,fitLin(længder,*val),label = 'Lineært fit')

#Og errorbars selvfølgelig. Jeg har i linje 22 ganget med 5 
#for at man her kan se dem integnet
plt.errorbar(længder,gns_tid,std_tid,ls='None')

#Jeg gør grafen læselig og pæn
plt.xlabel('Længde/[m]',fontsize = 15)
plt.ylabel('Tid/[ns]',fontsize = 15)
plt.grid()
plt.title('Lysets tøven som funktion af afstand')
plt.legend(fontsize = 13)
plt.show()


#Den fundne lyshastighed
calc = (1/val[0])

#Jeg ved at a-værdien af grafen må være hastigheden i enheden m/ns 
print("Hældningen på grafen er lig med " + str((calc)) + ", hvilket, hvis vi omregner enhederne, betyder at lysets hastigheden er målt til cirka:")

#Jeg ganger nu denne værdi med 10^9 for at få enheden m/s
calc *= 10**9

#Og SciPy har ogsp givet os usikkerheden, hvilket jeg også tager i m/s 
usikkerhed = math.floor(np.sqrt(cov[0,0]*10**9))

#Jeg printer også disse ting
print(str(math.floor(calc)) + " m/s ± " + str(usikkerhed) + " m/s")

#Jeg lader min dejlige computer konkludere for mig:
if(calc > c):
    print("hvilket desværre er lidt for højt, men næsten inden for usikkerheden.")
elif(calc < c):
    print("hvilket desværre er lidt for lavt, men næsten inden for usikkerheden.")
elif(calc == c):
    print("hvilket er helt præcist!!! Gud hvor er vi gode til Lab!!")#You have been Schauser-corrupted!!