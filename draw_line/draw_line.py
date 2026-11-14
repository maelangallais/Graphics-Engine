#Cree le 9 Mai 2024
from math import fabs as va,floor
from kandinsky import fill_rect as fr

n=(0,)*3
ent=lambda n:floor(n)if n-floor(n)<0.5 else floor(n)+1

def dl(x1,y1,x2,y2,t=1):
 w=h=1
 dx=min(max((x2-x1)/va(y2-y1)if va(y2-y1)!=0 else x2-x1,-1),1)
 dy=min(max((y2-y1)/va(x2-x1)if va(x2-x1)!=0 else y2-y1,-1),1)
 c=va(x2-x1)if va(x2-x1)>va(y2-y1)else va(y2-y1)
 if va(dx)<va(dy):w,x1,x2=t,x1-(t-1)//2,x2-(t-1)//2
 else:h,y1,y2=t,y1-(t-1)//2,y2-(t-1)//2
 for i in range(c):fr(ent(x1+dx*i),ent(y1+dy*i),w,h,n)

dl(0,0,320,222,10)
