#Créé le 13 Septembre 2023
from math import *
from kandinsky import *

def ent(n):
  if n-floor(n)<0.5:n=floor(n)
  else:n=ceil(n)
  return int(n)

n=(0,0,0)
b=(0,0,255)
w=(255,255,255)
v=(0,255,0)

r=100
d=r*2
cx,cy=160,111
hyp=r

fill_rect(320//2-d//2-1,222//2-d//2-1,d+2,d+2,b)
fill_rect(320//2-d//2,222//2-d//2,d,d,w)
fill_rect(320//2-d//2,222//2,d,1,n)
fill_rect(320//2,222//2-d//2,1,d,n)

for rep in range(2*r*pi):
  adj=cos(rep)*hyp
  x=cx+adj
  opp=sin(rep)*hyp
  y=cy+opp
  fill_rect(ent(x),ent(y),1,-2*ent(opp),v)
