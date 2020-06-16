import math
def Max2(a,b):
    if a>b:
        return a,b,a
    else:
        return a,b,b
def Max3(a,b,c):
    a,b,x=Max2(a,b)
    if x>c:
        return a,b,c,x
    else:
        return a,b,c,c
def Max4(a,b,c,d):
    a,b,c,x=Max3(a,b,c)
    if x>d:
        return a,b,c,d,x
    else:
        return a,b,c,d,d
def IsGanjil(N):
    if N>=0 and N%2!=0:
        return N,True
    else:
        return N,False
def IsPrima(N):
    for i in range(2,N):
        if N>1 and N%i==0:
            return N,False
        else:
            return N,True
    else:
        return N,True
def NumOfPrima(N):
    count=2
    numb=""
    while True:
        isprime = True
        for x in range(2, int(math.sqrt(count) + 1)):
            if count % x == 0:
                isprime = False
                break
        if count>N:
            break
        if isprime:
            numb=numb+str(count)+" "
        count += 1
    return N,numb
def Pangkat(basis, eksp):
    pangkat=basis**eksp
    return basis,eksp,pangkat
def SumOfN(N):
    sumData=0
    for i in range(0,N+1):
        sumData+=i
    return N,sumData
def ProductOfN(N):
    multiply=1
    for i in range(1,N+1):
        multiply*=i
    return N,multiply
def Average(N,count):
    sumData=0
    for i in range(0,N+1):
        sumData+=i
    ave=sumData/count
    return N,count,ave
def AveSumOfN(N):
    sumData=0
    count=0
    for i in range(1,N+1):
        sumData+=i
        count+=1
    ave=sumData/count
    return N,ave
def AveProdOfN(N):
    sumData=1
    count=0
    for i in range(1,N+1):
        sumData*=i
        count+=1
    ave=sumData/count
    return N,ave
def FPB(n,m):
    fct=0
    if n>m:
        fct=m
    else:
        fct=n
    for i in range(1,fct+1):
        if n%i==0 and m%i==0:
            fpb=i
    return n,m,fpb
def C2F(C):
    f=(9/5*C)+32
    return C,f
def F2C(F):
    c=5/9*(F-32)
    return F,c
def C2R(C):
    r=4/5*C
    return C,r
def R2C(R):
    c=5/4*R
    return R,c
def K2C(K):
    c=K+273
    return K,c
def C2K(C):
    k=C-273
    return C,k
def R2F(R):
    f=(9/4*R)+32
    return R,f
def F2R(F):
    r=4/9*(F-32)
    return F,r
