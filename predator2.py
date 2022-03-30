from turtle import *
import keyboard
from math import *

t1=Turtle()
t2=Turtle()
t1.stamp()
t1.color("green")
x1=-300
y1=300
x2=-100
y2=100
vx1=0
vy1=0
vx2=0
vy2=0

dt=.1
a=1 #player acceleration
A=30 #player constant speed
ma=1 #enemy acceleration
ev=30 #enemy constant speed
dd=10**-200

cont1=1
ded=1
while cont1==1:
    maxs=34 #28
    
    if keyboard.is_pressed("up arrow"):# and vy1<=maxs: #up
        vy1+=a
    if keyboard.is_pressed("down arrow"):# and vy1>=-maxs: #down
        vy1-=a
    if keyboard.is_pressed("left arrow"):# and vx1>=-maxs: #left
        vx1-=a
    if keyboard.is_pressed("right arrow"):# and vx1<=maxs: #right
        vx1+=a

    if vx1<0:
        cx=a
    if vx1>=0:
        cx=-a
    if vy1<0:
        cy=a
    if vy1>=0:
        cy=-a

    #player max v of 30
    sv=(vx1**2+vy1**2)**.5
    vx1=A*vx1/(sv+dd) #from a to maxs
    vy1=A*vy1/(sv+dd)

    #player position
    x1+=dt*vx1 
    y1+=dt*vy1

    #aiming
    corx1=(-vx1**2)/(2*cx) #x full brakes
    cory1=(-vy1**2)/(2*cy) #y full brakes

    timex=-vx1/cx #full throttle x
    fullvx=cx*timex+vx1
    corx2=(fullvx**2-vx1**2)/(2*cx)

    timey=-vy1/cy #full throttle y
    fullvy=cy*timey+vy1
    cory2=(fullvy**2-vy1**2)/(2*cy)

    corx=corx2
    cory=cory2
    #corx=(corx1+corx2)/2 #average throttle and brakes
    #cory=(cory1+cory2)/2

    r=((x1-x2)**2+(y1-y2)**2)**.5
    #print(r) #got 40 feet
    if r<40:
        corx,cory=0,0
        #print("ur ded",ded)
        ded+=1
        

    #corx=0
    #cory=0

    #correct aim position
    dx=x1-x2+corx
    dy=y1-y2+cory

    #move towards aim position
    r=(dx**2+dy**2)**.5

    
    ogvx=vx2
    ogvy=vy2
    vx2=ev*dx/(r) #vx2t
    vy2=ev*dy/(r) #A*
    
    if vx2-ogvx>ma: #acelerations
        vx2=ogvx+ma
    if ogvx-vx2>ma:
        vx2=ogvx-ma
    if vy2-ogvy>ma:
        vy2=ogvy+2
    if ogvy-vy2>ma:
        vy2=ogvy-ma

    
    x2+=vx2*dt
    y2+=vy2*dt

    bbox=400 #boundary box of 500 pixels square
    if -bbox>x1 or x1>bbox: #player x
        vx1*=-1
    if -bbox>y1 or y1>bbox:
        vy1*=-1
    if -bbox>x2 or x2>bbox:
        vx2*=-1
    if -bbox>y2 or y2>bbox:
        vy2*=-1
        

    t1.goto(x1,y1)
    t2.goto(x2,y2)

    #boundaries??







    
    








    
    
