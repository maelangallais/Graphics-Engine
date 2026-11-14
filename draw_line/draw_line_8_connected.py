#Cree le 22 Octobre 2026
from math import fabs as va,floor
from kandinsky import set_pixel as sp

n=(0,)*3
ent=lambda n:floor(n)if n-floor(n)<0.5 else floor(n)+1

#algorithme draw_line amélioré pour la 8-connectivité
def dl_8c(x1,y1,x2,y2):
 dx=min(max((x2-x1)/va(y2-y1)if va(y2-y1)!=0 else x2-x1,-1),1)
 dy=min(max((y2-y1)/va(x2-x1)if va(x2-x1)!=0 else y2-y1,-1),1)
 c=va(x2-x1)if va(x2-x1)>va(y2-y1)else va(y2-y1)
 px,py=x1,y1
 for i in range(c):
  nx,ny=x1+dx*i,y1+dy*i
  sp(ent(nx),ent(ny),n)
  if nx!=px and ny!=py:
   #The one or the other, it will set the extra
   #pixel above or under the completed square
   sp(ent(px),ent(ny),n)
   #sp(ent(nx),ent(py),n)
  px,py=nx,ny

dl(0,0,320,222)
