def FunctionSatu(n):
    nNext=n
    while True:
        n=nNext%10
        if n==1:
            n=True
            break
        else:
            nNext=nNext//10
            if nNext<1:
                n=False
                break
    return n
def FunctionFactor(n):
    nFirst=n
    nNext=n
    while True:
        n=nNext%10
        if n==0:
            n=False
            break
        elif nFirst%n!=0:
            n=False
            break
        else:
            nNext=nNext//10
            if nNext<1:
                n=True
                break
    return n
def FunctionAkhir1(a,b):
    a=a%10
    b=b%10
    if a==b:
        return True
    else:
        return False
def FunctionAkhir2(a,b,p):
    p=10**p
    a=a%p
    b=b%p
    if a==b:
        return True
    else:
        return False
def main():
    n1=FunctionSatu(10)
    n2=FunctionFactor(128)
    n3=FunctionAkhir1(3,113)
    n4=FunctionAkhir2(3,113,2)
    print(n1)
    print(n2)
    print(n3)
    print(n4)
if __name__ == '__main__':
    main()
