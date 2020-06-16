import math
MP={}
def MakePoint(a,b,T):
    global MP
    MP[T+"Absis"]=a
    MP[T+"Ordinat"]=b
    return MP
def GetAbsis(T):
    return MP[T+"Absis"]
def GetOrdinat(T):
    return MP[T+"Ordinat"]
def SetOrdinat(newx,T):
    global MP
    MP[T+"Ordinat"]=newx
    return MP[T+"Ordinat"]
def SetAbsis(newy,T):
    global MP
    MP[T+"Absis"]=newy
    return MP[T+"Absis"]
def BacaPoint(T):
    x,y=map(int, input("P{} x,y : ".format(T)).split(','))
    p=MakePoint(x,y,T)
    Tulis(p,T)
def Tulis(p,T):
    print("P{}: ({},{})".format(T,p[T+"Absis"],p[T+"Ordinat"]))
def AddP(x1,y1,x2,y2):
    return x1+x2,y1+y2
def MinP(x1,y1,x2,y2):
    return x1-x2,y1-y2
def MulDot(x1,y1,x2,y2):
    return x1*x2,y1*y2
def IsEqual(x1,y1,x2,y2):
    return (x1==x2 and y1==y2)
def IsNotEqual(x1,y1,x2,y2):
    return (x1!=x2 or y1!=y2)
def IsLess(x1,y1,x2,y2):
    return (x1+y1<x2+y2)
def IsGreater(x1,y1,x2,y2):
    return (x1+y1>x2+y2)
def IsOrigin(x,y):
    return (x==0 and y==0)
def IsOnSbX(x):
    return (x==0)
def IsOnSbY(y):
    return (y==0)
def Kuadran(x,y):
    if x>0 and y>0:
        return "1"
    elif x<0 and y>0:
        return "2"
    elif x>0 and y<0:
        return "4"
    elif x<0 and y<0:
        return "3"
    else:
        return "Titik berada pada sumbu x,y atau 0,0"
def NextX(x,T):
    global MP
    MP[T+"Absis"]=x+1
    return MP[T+"Absis"]
def NextY(y,T):
    global MP
    MP[T+"Ordinat"]=y+1
    return MP[T+"Ordinat"]
def PlusDelta(x,y,deltax,deltay,T):
    global MP
    MP[T+"Absis"]=x+deltax
    MP[T+"Ordinat"]=y+deltay
    return MP[T+"Absis"],MP[T+"Ordinat"]
def MirrorOf(x,y,sb,T):
    global MP
    if sb=="SbX":
        MP[T+"Ordinat"]=((-1)*y)
        return x,MP[T+"Ordinat"]
    elif sb=="SbY":
        MP[T+"Absis"]=((-1)*x)
        return MP[T+"Absis"],y
def JarakPst(x,y):
    return "{:.2f}".format(math.sqrt((x**2)+(y**2)))
def Jarak2T(x1,y1,x2,y2):
    return "{:.2f}".format(math.sqrt(((x2-x1)**2)+((y2-y1)**2)))
def Geser(x,y,deltax,deltay,T):
    global MP
    MP[T+"Absis"]=x+deltax
    MP[T+"Ordinat"]=y+deltay
    return MP[T+"Absis"],MP[T+"Ordinat"]
def GeserSbX(x,deltax,T):
    global MP
    MP[T+"Absis"]=x+deltax
    return MP[T+"Absis"]
def GeserSbY(y,deltay,T):
    global MP
    MP[T+"Ordinat"]=y+deltay
    return MP[T+"Ordinat"]
def MirrorP(x,y,sb,T):
    global MP
    if sb=="SbX":
        MP[T+"Ordinat"]=((-1)*y)
        return x,MP[T+"Ordinat"]
    elif sb=="SbY":
        MP[T+"Absis"]=((-1)*x)
        return MP[T+"Absis"],y
def Putar(x,y,sudut):
    return (math.cos(sudut)*x)+(math.sin(sudut)*y),((-1)*math.sin(sudut)*x)+(math.cos(sudut)*y)
