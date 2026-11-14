#Créé le 18 Septembre 2025
from kandinsky import fill_rect as fr,set_pixel as sp

#pas d'épaisseur et pas optimisé
def circle1(cx,cy,r,col):
 r=int(r)
 R=r<<1
 r2=r*r
 for a in range(R):
  dx=a-r
  dx2=dx*dx
  for b in range(R):
   dy=b-r
   if dx2+dy*dy<=r2:
    sp(cx+dx,cy+dy,col)

#pas optimisé mais avec épaisseur
def circle2(cx,cy,r,t,col):
 r=int(r)
 t=min(r,t)
 R=r<<1
 r2=r*r
 rt2=(r-t)*(r-t)
 for a in range(R):
  dx=a-r
  dx2=dx*dx
  for b in range(R):
   dy=b-r
   dst2=dx2+dy*dy
   if dst2<=r2 and dst2>=rt2:
    sp(cx+dx,cy+dy,col)

#optimisé sans épaisseur
def circle3(cx,cy,r,col):
 x,y=r,0
 d=1-r
 while x>=y:
  fr(cx-x,cy+y,2*x,1,col)
  fr(cx-x,cy-y,2*x,1,col)
  fr(cx-y,cy+x,2*y,1,col)
  fr(cx-y,cy-x,2*y,1,col)
  y+=1
  if d<=0:
   d+=2*y+1
  else:
   x-=1
   d+=2*(y-x)+1

#optimisé avec épaisseur mais mal pensé
def circle4(cx,cy,r,t,col):
 t=min(r,t())
 t2=(r-t)*(r-t)
 x,y=r,0
 d=1-r
 while x>=y:
  x2,y2=x*x,y*y
  for i in range(2*x):
   xi=-x+i
   if xi*xi+y2>=t2:
    cxxi=cx+xi
    sp(cxxi,cy+y,col)
    sp(cxxi,cy-y,col)
  for i in range(2*y):
   yi=-y+i
   if yi*yi+x2>=t2:
    cxyi=cx+yi
    sp(cxyi,cy+x,col)
    sp(cxyi,cy-x,col)
  y+=1
  if d<=0:
   d+=2*y+1
  else:
   x-=1
   d+=2*(y-x)+1

#optimisé au max avec épaisseur
def circle5(cx,cy,r,t,col):
 t=min(r,t)
 ri=r-t #r_inner
 x,y=r,0
 d=1-r
 while x>=y:
  tx=int((max(ri*ri-y*y,0))**.5)
  ty=int((max(ri*ri-x*x,0))**.5)
  xmtx,ymty=x-tx,y-ty
  fr(cx-x,cy+y,(xmtx),1,col)
  fr(cx-x,cy-y,(xmtx),1,col)
  fr(cx-y,cy+x,(ymty),1,col)
  fr(cx-y,cy-x,(ymty),1,col)
  fr(cx+tx,cy+y,(xmtx),1,col)
  fr(cx+tx,cy-y,(xmtx),1,col)
  fr(cx+ty,cy+x,(ymty),1,col)
  fr(cx+ty,cy-x,(ymty),1,col)
  y+=1
  if d<=0:
   d+=2*y+1
  else:
   x-=1
   d+=2*(y-x)+1
