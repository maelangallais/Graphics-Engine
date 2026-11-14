#Créé le 20 Octobre 2026

from math import *
from kandinsky import *
from time import *

add, sub=lambda a,b:a+b, lambda a,b:a-b

def d(x,y,r,a,c):
  s=ceil(2*pi*r)
  ai=radians(a)
  op=add if c else sub
  iop=sub if c else add
  for i in range(s):
    ag=iop(i/s*2*pi,ai)
    xp=x+r*cos(ag)
    yp=op(y,r*sin(ag))
    set_pixel(round(xp),round(yp),(0,)*3)
    sleep(0.01)

d(160,111,20,36,0)
