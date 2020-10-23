import numpy as np
import matplotlib.pyplot as plt
#You have been Schauser-corrupted!!



def fjederpendul(o,x,n):
    dt = 0.05
    k=1
    
    fig, ax = plt.subplots()


    pos = lambda o,x: [np.cos(o)*x,np.sin(o)*x]
    
    ball = ax.scatter(*pos(o,x))
    line, = ax.plot([0,pos(o,x)[0]],[0,pos(o,x)[1]])
    
    ts = []
    m = 1
    g = 9.8
    vo = 1
    vx = 0
    for i in range(n):
        #plt.cla()
        ax.set_xlim(-10,10)
        ax.set_ylim(-10,10)
        vo += -(2*vo*vx+np.sin(o)*x*g)/x**2*dt
        o += vo*dt
        vx += (vo**2*x - (1-np.cos(o))*g - (k/m)*x)*dt
        x += vx*dt
        #print(pos(o,x))
        ball.set_offsets(pos(o,x))
        line.set_ydata([0,pos(o,x)[1]])
        line.set_xdata([0,pos(o,x)[0]])
        plt.show()
        plt.pause(0.1)

fjederpendul(-1,0.7,500)
