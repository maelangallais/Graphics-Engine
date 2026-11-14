#Créé le 13 Septembre 2023
from math import *
from kandinsky import *

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
  x=cx+r*cos(rep)
  y=cy+r*sin(rep)
#Cela revient a utiliser la trigonometrie:
# adj=cos(rep)*hyp
# x=cx+adj
# opp=sin(rep)*hyp
# y=cy+opp
  set_pixel(int(x),int(y),v)
