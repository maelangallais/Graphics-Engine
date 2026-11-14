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
  for y in range(h):
    for x in range(w):
      c=0
      p=False
      for z in range(w-x):
        """
C'est ici qu'il faudra améliorer les calculs
Il compte tous les coins comme une seule intersection
là où il faudrait en compter deux : 
 - un trait qui arrive
 - un trait qui repart
La solution serait peut-être de vérifier l'angle
de chaque côté à chaque intersection pour vérifier que
c'est un angle ou une surface plate et la compter ou non
Sinon passer toutes mes lignes en courbes de bezier
pour éviter les get_pixel() et privilégier les 
calculs théoriques absolus sur des formes plutôt que
sur ce que l'on peut voir à l'écran
Superbe vidéo sur le sujet : 
https://www.youtube.com/watch?v=SO83KQuuZvg
"""
        if get_pixel(wo+(x+z)*t,ho+y*t)==col:
          if p:
            continue
          c+=1
          p=True
        elif p:
          p=False
      if c%2:
        for a in range(t):
          for b in range(t):
            set_pixel(wo+x*t+a,ho+y*t+b,col)

draw([[19,2],[43,187],[134,98]])
draw([[232,67],[187,122],[308,208]])
draw([[120,12],[180,53],[210,23],[312,87],[275,7]])
circle(150,170,40,col)

fill()
