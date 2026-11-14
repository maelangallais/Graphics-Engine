#Créé le 3 Mai 2023
from kandinsky import set_pixel
from random import randint

ch,c=1,(randint(0,255),randint(0,255),randint(0,255))
if ch==1:
  print("Warning : s'il ne se passe rien c'est")
  print("parce que le triangle est trop plat !")
  co1=input("Entrez coordonnées 1er point : ")
  co2=input("Entrez coordonnées 2eme point : ")
  co3=input("Entrez coordonnées 3eme point : ")
  cox1,coy1=co1.split(',')
  cox2,coy2=co2.split(',')
  cox3,coy3=co3.split(',')
elif ch==2:
  cox1,coy1=40,50
  cox2,coy2=240,50
  cox3,coy3=140,200
cox1,coy1,cox2,coy2,cox3,coy3=int(cox1),int(coy1),int(cox2),int(coy2),int(cox3),int(coy3)

if cox1<0 or cox1>320 or cox2<0 or cox2>320 or cox3<0 or cox3>320 or coy1<0 or coy1>222 or coy2<0 or coy2>222 or coy3<0 or coy3>222:
  print("Tu te crois drôle ?")
  return
if cox1==cox2 and cox1==cox3 or coy1==coy2 and coy1==coy3:
  print("Tu te crois drôle ?")
  return

set_pixel(cox1,coy1,(255,0,0))
set_pixel(cox2,coy2,(255,0,0))
set_pixel(cox3,coy3,(255,0,0))

if coy1==coy2 or coy2==coy3 or coy1==coy3:
  if coy1==coy2:
    if cox2>coy1:cog,cod=cox1,cox2+1
    else:cog,cod=cox2,cox1+1
    if coy3>coy1:h,hb=coy3-coy1,2
    else:h,hb=(coy1-coy3)+1,1
    x,y=cox3,coy3
  elif coy1==coy3:
    if cox3>coy1:cog,cod=cox1,cox3+1
    else:cog,cod=cox3,cox1+1
    if coy2>coy1:h,hb=coy2-coy1,2
    else:h,hb=(coy1-coy2)+1,1
    x,y=cox2,coy2
  elif coy2==coy3:
    if cox2>coy3:cog,cod=cox3,cox2+1
    else:cog,cod=cox2,cox3+1
    if coy1>coy3:h,hb=coy1-coy3,2
    else:h,hb=(coy3-coy1)+1,1
    x,y=cox1,coy1
  coo=x
  if hb==1:
    r=1
    for a in range(h):
      for b in range(r):
        set_pixel(int(x),int(y),c)
        x+=1
      x-=(coo-cog)/h+r+0.5
      if coo<cod:r+=((cod-coo)/h+((coo-cog)/h-0.5))+0.5
      else:r+=(coo-cod)/h+(coo-cog)/h-0.5
      y+=1
  elif hb==2:
    r=1
    for a in range(h+1):
      for b in range(r):
        set_pixel(int(x),int(y),c)
        x+=1
      x-=(coo-cog)/h+r+0.5
      if coo<cod:r+=((cod-coo)/h+((coo-cog)/h-0.5))+0.5
      else:r+=(coo-cod)/h+(coo-cog)/h-0.5
      y-=1

else:
  if coy1<coy2 and coy1<coy3:
    x1,y1=cox1,coy1
    if coy3>coy2:
      x2,y2=cox2,coy2
      x3,y3=cox3,coy3
    else:
      x2,y2=cox3,coy3
      x3,y3=cox2,coy2
  elif coy2<coy1 and coy2<coy3:
    x1,y1=cox2,coy2
    if coy3>coy1:
      x2,y2=cox1,coy1
      x3,y3=cox3,coy3
    else:
      x2,y2=cox3,coy3
      x3,y3=cox1,coy1
  elif coy3<coy1 and coy3<coy2:
    x1,y1=cox3,coy3
    if coy2>coy1:
      x2,y2=cox1,coy1
      x3,y3=cox2,coy2
    else:
      x2,y2=cox2,coy2
      x3,y3=cox1,coy1

  hy1,hy2=y2-y1,y3-y2
  hy3=hy1+hy2
  x,y=x1,y1

  if x2<x3:
    r=1
    for a in range(hy1):
      for b in range(r):
        set_pixel(int(x),int(y),c)
        x+=1
      x-=(x1-x2)/hy1+r+0.5
      r+=(x3-x1)/hy3+((x1-x2)/hy1)
      y+=1
    for a in range(hy2+1):
      for b in range(r):
        set_pixel(int(x),int(y),c)
        x+=1
      x-=(x2-x3)/hy2+r+0.5
      r+=(x3-x1)/hy3+((x2-x3)/hy2)
      y+=1
  else:
    r=1
    for a in range(hy1):
      for b in range(r):
        set_pixel(int(x),int(y),c)
        x+=1
      x-=(x1-x3)/hy3+r+0.5
      r+=(x2-x1)/hy1-((x3-x1)/hy3)
      y+=1
    for a in range(hy2+1):
      for b in range(r):
        set_pixel(int(x),int(y),c)
        x+=1
      x-=(x1-x3)/hy3+r+0.5
      r-=(x2-x3)/hy2+((x3-x1)/hy3)
      y+=1
