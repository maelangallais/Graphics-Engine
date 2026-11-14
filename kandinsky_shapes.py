#Cree le 26 Mars 2023
from kandinsky import set_pixel
from random import randint
from math import sin,cos,pi,floor

ent=lambda n:floor(n)if n-floor(n)<0.5 else floor(n)+1
c=randint(0,255),randint(0,255),randint(0,255)

def instructions():
  print(" ")
  print(" ")
  print("Il y a 5 fonctions à tester :")
  print("La 1ère fait les rectangle.")
  print("La 2ème fait les triangles.")
  print("La 3ème fait les pavés droits.")
  print("La 4ème fait les rectangles penchés.")
  print("La 5ème fait les ronds et cercles.")
  print("Toutes les figures sont centrés sur l'écran.")
  print("Et pour les alternatives le 'x,y'")
  print("détermine la position, le 'w' la hauteur et")
  print("le 'h' la longueur, 'c' c'est la couleur")
  print("si vous mettez 'c' ce sera aléatoire.")
  fonction=input("Choisir 1, 2, 3, 4 ou 5 : ")
  resultat=eval(fonction)
  if resultat==1:
    print(" ")
    print(" ")
    print("Le 1er fait 1 rectangle multicolor.")
    print("  -Alternative : rectan(x,y,w,h,c).")
    print("Le 2eme fait 1 rectangle unicolor.")
    print("  -Alternative : rect(x,y,w,h,c).")
    t=input("Quel rectangle (3=alternatives) ? ")
    n=eval(t)
    if n==1:
      rectangle()
    if n==2:
      rectoo()
    if n==3:
      print("Ecrire l'alternative :")  
  if resultat==2:
    print(" ")
    print(" ")
    print("Le 1er fait 1 triangle pointe vers le haut.")
    print("  -Alternative : trihau(x,y,w,h,c).")
    print("Le 2eme fait 1 triangle pointe vers le bas.")
    print("  -Alternative : tribas(x,y,w,h,c).")
    print("Le 3eme fait 1 triangle pointe vers la droite.")
    print("  -Alternative : tridroi(x,y,w,h,c).")
    print("Le 4eme fait 1 triangle pointe vers la gauche.")
    print("  -Alternative : trigau(x,y,w,h,c).")
    t=input("Quel triangle (5=alternatives) ? ")
    n=eval(t)
    if n==1:
      triangle_haut()
    if n==2:
      triangle_bas()
    if n==3:
      triangle_droite()
    if n==4:
      triangle_gauche()
    if n==3:
      print("Ecrire l'alternative :")  
  if resultat==3:
    print(" ")
    print(" ")
    print("Le 1er fait 1 parallepipede vers la droite.")
    print("  -Alternative : paradroi(x,y,w,h,c).")
    print("Le 2eme fait 1 parallepipede vers la gauche.")
    print("  -Alternative : paragau(x,y,w,h,c).")
    t=input("Quel parallepipede (3=alternatives) ? ")
    n=eval(t)
    if n==1:
      parallepipede_droit()
    if n==2:
      parallepipede_gauche()
    if n==3:
      print("Ecrire l'alternative :")  
  if resultat==4:
    print(" ")
    print(" ")
    print("Le 1er fait 1 rectangle penché vers la droite.")
    print("  -Alternative : rectpendroi(x,y,w,h,c).")
    print("Le 2eme fait 1 rectangle penché vers la gauche.")
    print("  -Alternative : rectpengau(x,y,w,h,c).")
    t=input("Quel rectangle penché (3=alternatives) ? ")
    n=eval(t)
    if n==1:
      rectangle_penche_droite()
    if n==2:
      rectangle_penche_gauche()
    if n==3:
      print("Ecrire l'alternative :")
  elif resultat==5:
    print(" ")
    print(" ")
    print("Le 1er fait un rond(plein).")
    print(" -Alternative : rond(x,y,r,c).")
    print("Le 2ème fait un cercle(périmètre).")
    print(" -Alternative : cercle(x,y,r,w,c).")
    t=input("Rond ou cercle (3=alternatives) ? ")
    n=eval(t)
    if n==1:
      fround()
    if n==2:
      circle()
    if n==3:
      print("Ecrire l'alternative :")

def rectangle():
  print(" ")
  print(" ")
  b=int(input("Combien de largeur fera le rectangle ? "))
  d=int(input("Combien de hauteur fera le rectangle ? "))
  x=159-b//2
  y=110+d//2
  for a in range(b):
    y-=d
    x+=1
    for e in range(d):
      y+=1
      set_pixel(x,y,(randint(0,255),randint(0,255),randint(0,255)))

def rectan(x,y,w,h,c):
  for a in range(w):
    for b in range(h):
      set_pixel(x+a,y+b,(randint(0,255),randint(0,255),randint(0,255)))

def rectoo():
  print(" ")
  print(" ")
  b=int(input("Combien de largeur fera le rectangle ? "))
  d=int(input("Combien de hauteur fera le rectangle ? "))
  for f in range(b):
    for g in range(d):
      set_pixel(160-b//2+f,111-d//2+g,(randint(0,255),randint(0,255),randint(0,255)))

def rect(x,y,w,h,c):
  for a in range(w):
    for b in range(h):
      set_pixel(x+a,y+b,c)

def triangle_haut():
  print(" ")
  print(" ")
  h=int(input("Combien de hauteur fera le triangle ? "))
  i=int(input("Quel sera la base du triangle ? "))
  if h<i:
    m=160
    l=int(111-h/2)
    n=1
    for j in range(h):
      for k in range(n):
        set_pixel(m,l,c)
        m+=1
      m-=i//h+n
      n+=i//h*2
      l+=1
  else:
    m=160-i//2
    l=111+h//2
    n=1
    for j in range(i//2):
      for k in range(n):
        set_pixel(m,l,c)
        l-=1
      l+=n
      n+=h//i*2
      m+=1
    for j in range(i//2):
      for k in range(n):
        set_pixel(m,l,c)
        l-=1
      l+=n
      n-=h//i*2
      m+=1
    

def trihau(x,y,w,h,c):
  s=1
  for j in range(h):
    for k in range(s):
      set_pixel(x,y,c)
      x+=1
    x-=w//h+s
    y+=1
    s+=w//h*2

def triangle_bas():
  print(" ")
  print(" ")
  h=int(input("Combien de hauteur fera le triangle ? "))
  i=int(input("Quel sera la base du triangle ? "))
  if h<i:
    m=160
    l=111+h//2
    n=1
    for j in range(h):
      for k in range(n):
        set_pixel(m,l,c)
        m+=1
      m-=i//h+n
      n+=i//h*2
      l-=1
  else:
    m=160-i//2
    l=111-h//2
    n=1
    for j in range(i//2):
      for k in range(n):
        set_pixel(m,l,c)
        l+=1
      l-=n
      n+=h//i*2
      m+=1
    for j in range(i//2):
      for k in range(n):
        set_pixel(m,l,c)
        l+=1
      l-=n
      n-=h//i*2
      m+=1

def tribas(x,y,w,h,c):
  if h<w:
    n=1
    for j in range(h):
      for k in range(n):
        set_pixel(x,y,c)
        x+=1
      x-=w//h+n
      n+=w//h*2
      y-=1
  else:
    n=1
    for j in range(w//2):
      for k in range(n):
        set_pixel(x,y,c)
        y+=1
      y-=n
      n+=h//w*2
      x+=1
    for j in range(w//2):
      for k in range(n):
        set_pixel(x,y,c)
        y+=1
      y-=n
      n-=h//w*2
      x+=1

def triangle_droite():
  print(" ")
  print(" ")
  h=int(input("Combien de hauteur fera le triangle ? "))
  l=int(input("Quel sera la base du triangle ? "))
  x=160+h//2
  y=111
  n=1
  for j in range(h):
    for k in range(n):
      set_pixel(x,ent(y),c)
      y-=1
    y=111+n/2
    x-=1
    n+=l/h

def tridroi(x,y,w,h,c):
  s,y2=1,y
  for j in range(h):
    for k in range(s):
      set_pixel(x,ent(y),c)
      y-=1
    y=y2+s/2
    x-=1
    s+=w/h

def triangle_gauche():
  print(" ")
  print(" ")
  h=int(input("Combien de hauteur fera le triangle ? "))
  l=int(input("Quel sera la base du triangle ? "))
  x=160-h//2
  y=111
  n=1
  for j in range(h):
    for k in range(n):
      set_pixel(x,ent(y),c)
      y-=1
    y=111-n/2
    x+=1
    n+=l/h

def trigau(x,y,w,h,c):
  s,y2=1,y
  for j in range(h):
    for k in range(s):
      set_pixel(x,ent(y),c)
      y+=1
    y=y2-n/2
    x+=1
    s+=w/h

def parallepipede_droit():
  print(" ")
  print(" ")
  print("Combien de hauteur fera le parallépipède ? ")
  o=int(input())
  print("Combien de largeur fera le parallépipède ? ")
  p=int(input())
  s=160-p
  t=110-o//2
  for q in range(o):
    for r in range(p):
      s+=1
      set_pixel(s,t,c)
    s-=p
    t+=1
    s+=1

def paradroi(x,y,w,h,c):
  for a in range(w):
    for b in range(h):
      x+=1
      set_pixel(x,y,c)
    x-=h
    y+=1
    x+=1

def parallepipede_gauche():
  print(" ")
  print(" ")
  print("Combien de hauteur fera le parallépipède ? ")
  o=int(input())
  print("Combien de largeur fera le parallépipède ? ")
  p=int(input())
  s=160
  t=110-o//2
  for q in range(o):
    for r in range(p):
      s+=1
      set_pixel(s,t,c)
    s-=p
    t+=1
    s-=1

def paragau(x,y,w,h,c):
  for a in range(w):
    x-=h
    y+=1
    x-=1
    for b in range(h):
      x+=1
      set_pixel(x,y,c)

def rectangle_penche_droite():
  print(" ")
  print(" ")
  print("Combien de hauteur fera le rectangle penché ? ")
  h=int(input())
  print("Combien de largeur fera le rectangle penché ? ")
  l=int(input())
  x=160
  y=111-h//2
  w=l
  for u in range(l):
    for v in range(w):
      set_pixel(x,y,c)
      x-=1
    x-=l//l-w
    y-=1
    w-=l//l*2
  x=159
  y=110-h//2
  for q in range(h):
    x-=l
    y+=1
    x+=1
    for r in range(l):
      x+=1
      set_pixel(x,y,c)
  w=l
  for u in range(l):
    for v in range(w):
      set_pixel(x,y,c)
      x-=1
    x-=l//l-w
    y+=1
    w-=l//l*2

def rectpendroi(x,y,w,h,c):
  x1=x+h
  y1=y
  c1=c
  c2=c
  s=h
  for a in range(h):
    for b in range(s):
      set_pixel(x1,y1,c)
      x1-=1
    x1-=w//w-s
    y1-=1
    s-=h//h*2
  for c in range(w):
    for d in range(h):
      x+=1
      set_pixel(x,y,c1)
    x-=h
    y+=1
    x+=1
  s=h
  x+=h
  for e in range(h):
    for f in range(s):
      set_pixel(x,y,c2)
      x-=1
    x-=h//h-s
    y+=1
    s-=h//h*2

def rectangle_penche_gauche():
  print(" ")
  print(" ")
  print("Combien de hauteur fera le rectangle penché ? ")
  h=int(input())
  print("Combien de largeur fera le rectangle penché ? ")
  l=int(input())
  x=160+l
  y=111-h//2
  w=l
  for u in range(l):
    for v in range(w):
      set_pixel(x,y,c)
      x-=1
    x-=l//l-w
    y-=1
    w-=l//l*2
  x=161+l
  y=110-h//2
  for q in range(h):
    x-=l
    y+=1
    x-=1
    for r in range(l):
      x+=1
      set_pixel(x,y,c)
  w=l
  for u in range(l):
    for v in range(w):
      set_pixel(x,y,c)
      x-=1
    x-=l//l-w
    y+=1
    w-=l//l*2

def rectpengau(x,y,w,h,c):
  x1=x
  y1=y
  c1=c
  c2=c
  s=h
  for a in range(h):
    for b in range(s):
      set_pixel(x1,y1,c)
      x1-=1
    x1-=w//w-s
    y1-=1
    s-=h//h*2
  for c in range(w):
    x-=h
    y+=1
    x-=1
    for d in range(h):
      x+=1
      set_pixel(x,y,c1)
  s=h
  for e in range(h):
    for f in range(s):
      set_pixel(x,y,c2)
      x-=1
    x-=h//h-s
    y+=1
    s-=h//h*2

def fround():
  cx=160
  cy=111
  r=int(input("Quel rayon ? "))
  for rep in range(10*r*pi):
    adj=cos(rep)*r
    x=cx+adj
    opp=sin(rep)*r
    y=cy+opp
    for i in range(-2*int(opp)):
      set_pixel(int(x),int(y)+i,c)

def rond(cx,cy,r,c):
   for rep in range(10*r*pi):
    adj=cos(rep)*r
    x=cx+adj
    opp=sin(rep)*r
    y=cy+opp
    for i in range(-2*int(opp)):
      set_pixel(int(x),int(y)+i,c)

def circle():
  cx=160
  cy=111
  r=int(input("Quel rayon ? "))
  w=int(input("Épaisseur du cercle ? "))
  for i in range(w):
    x,y,d=0,r,3-2*r
    while x<=y:
      set_pixel(cx+x,cy+y,c)
      set_pixel(cx-x,cy+y,c)
      set_pixel(cx+x,cy-y,c)
      set_pixel(cx-x,cy-y,c)
      set_pixel(cx+y,cy+x,c)
      set_pixel(cx-y,cy+x,c)
      set_pixel(cx+y,cy-x,c)
      set_pixel(cx-y,cy-x,c)
      if d<0:
        d=d+4*x+6
      else:
        d=d+4*(x-y)+10
        y=y-1
      x=x+1
    r-=1

def cercle(cx,cy,r,w,c):
  for i in range(w):
    x,y,d=0,r,3-2*r
    while x<=y:
      set_pixel(cx+x,cy+y,c)
      set_pixel(cx-x,cy+y,c)
      set_pixel(cx+x,cy-y,c)
      set_pixel(cx-x,cy-y,c)
      set_pixel(cx+y,cy+x,c)
      set_pixel(cx-y,cy+x,c)
      set_pixel(cx+y,cy-x,c)
      set_pixel(cx-y,cy-x,c)
      if d<0:
        d=d+4*x+6
      else:
        d=d+4*(x-y)+10
        y=y-1
      x=x+1
    r-=1

instructions()
