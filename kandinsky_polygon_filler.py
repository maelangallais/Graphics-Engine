#Créé le 11 Novembre 2026
from kandinsky import set_pixel,get_pixel

ent=lambda n:int(n+0.5)
va=lambda x:-x if x<0 else x
col=(0,)*3
ifc=(255,182,57)

#Relatif à la taille
t=3
w=320//t
h=222//t
wo=320-w*t
ho=222-h*t
for y in range(ho):
  for x in range(320):
    set_pixel(x,y,ifc)
for x in range(wo):
  for y in range(222):
    set_pixel(x,y,ifc)

#Version optimisée pour ne faire que des traits de 1 d'épaisseur
#Mais tout est gâché avec la double boucle for pour simuler un carré
def dl(p1,p2,col):
 [x1,y1],[x2,y2]=p1,p2
 dx=min(max((x2-x1)/va(y2-y1)if va(y2-y1)!=0 else x2-x1,-1),1)
 dy=min(max((y2-y1)/va(x2-x1)if va(x2-x1)!=0 else y2-y1,-1),1)
 c=va(x2-x1)if va(x2-x1)>va(y2-y1)else va(y2-y1)
 for i in range(c):
   for x in range(t):
     for y in range(t):
       set_pixel(wo+ent((x1+dx*i)/t)*t+x,ho+ent((y1+dy*i)/t)*t+y,col)

def draw(*val):
  val=list(val[0])
  if len(val)<3:
    print("La liste doit contenir")
    print("au moins 3 points pour")
    print("dessiner une forme fermée.")
    return 1
  for i in range(len(val)):
    p0=val[i]
    p1=val[(i+1)%len(val)]
    dl(p0,p1,col)

from math import sin,cos,pi
def circle(x,y,r,col):
  s=int(2*pi*r/t)+1
  for i in range(s):
    ag=i/s*2*pi
    xp=x+r*cos(ag)
    yp=y+r*sin(ag)
    for a in range(t):
      for b in range(t):
        set_pixel(wo+ent(xp/t)*t+a,ho+ent(yp/t)*t+b,col)

def fill():
  gp=lambda x,y:get_pixel(wo+x*t,ho+y*t)==col
  def de(y,x1,x2,dy):
    for _ in range(12):
      ny=y+dy
      if not(0<=ny<h):
        return 1
      nx1=-1
      for x in range(max(0,x1-1),min(w,x2+2)):
        if gp(x,ny):
          if nx1<0:
            nx1=nx2=x
            while nx1>0 and gp(nx1-1,ny):
              nx1-=1
            while nx2+1<w and gp(nx2+1,ny):
              nx2+=1
          elif x>nx2:
            return 0
      if nx1<0:
        return 1
      for x in range(max(0,nx1-1),min(w,nx2+2)):
        if(x<x1-1 or x>x2+1)and gp(x,y):
          return 0
      x1,x2,y=nx1,nx2,ny
    return 0
  Q=[]
  for y in range(h+13):
    if y<h:
      c=px=x=0
      sp=[]
      while x<w:
        if gp(x,y):
          x1=x
          while x+1<w and gp(x+1,y):
            x+=1
          if c%2 and px<x1:
            sp.append((px,x1))
          c+=2 if de(y,x1,x,-1)or de(y,x1,x,1)else 1
          px=x+1
        x+=1
      Q.append(sp)
    if y>=13:
      for x1,x2 in Q.pop(0):
        for x in range(x1,x2):
          for a in range(t):
            for b in range(t):
              set_pixel(wo+x*t+a,ho+(y-13)*t+b,col)

draw([[19,2],[43,187],[134,98]])
draw([[232,67],[187,122],[308,208]])
draw([[120,12],[180,53],[210,23],[312,87],[275,7]])
circle(150,170,40,col)

fill()
