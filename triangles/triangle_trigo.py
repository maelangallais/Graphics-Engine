#Créé le 22 Février 2023
from kandinsky import set_pixel

def triangle():
  h=int(input("Combien de hauteur fera le triangle ? "))
  w=int(input("Quel sera la base du triangle ? "))
  x=160
  y=111-h/2
  r=1
  for a in range(h):
    for b in range(r):
      set_pixel(int(x),int(y),(255,0,0))
      x+=1
    x-=w/h+r
    r+=w/h*2
    y+=1

def bresenham():
  h=int(input("Combien de hauteur fera le triangle ? "))
  w=int(input("Quel sera la base du triangle ? "))
  x=160-h//2
  y=111+w//4
  for a in range(w):
    for b in range(h):
      if a<=b*w//h and a<=(h-b-1) * w//h:
        set_pixel(x+b,y-a,(255,0,0))

print("Entrez triangle() ou bresenham()")
