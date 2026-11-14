#Créé le 15 Septembre 2023
from math import *
from kandinsky import *

def ent(n):
  if n-floor(n)<0.5:n=floor(n)
  else:n=ceil(n)
  return int(n)

def rond(cx,cy,r,c):
  hyp=r
  for rep in range(2*r*pi):
    adj=cos(rep)*hyp
    x=cx+adj
    opp=sin(rep)*hyp
    y=cy+opp
    fill_rect(ent(x),ent(y),1,-2*ent(opp),c)

def cercle(cx,cy,r,width,c):
  for i in range(width):
    r-=1
    for ang in range(2*r*pi):
      x=cx+r*cos(ang)
      y=cy+r*sin(ang)
      set_pixel(ent(x),ent(y),c)

rond(160,111,100,(255,200,0))
rond(100,111,40,(255,100,0))
rond(220,111,40,(255,100,0))
rond(160,51,40,(255,100,0))
rond(160,171,40,(255,100,0))
cercle(160,111,110,2,(0,0,255))
