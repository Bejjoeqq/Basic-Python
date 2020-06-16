def panjang(data):
    count=0
    if data==None:
        return count
    else:
        for i in data:
            count+=1
    return count
def bacaTabelInt():
    data=[x for x in map(int, input("Tabel Int : ").split(","))]
    if panjang(data)>20:
        data=data[:20]
    return data
def bacaTabelFloat():
    data=[x for x in map(float, input("Tabel Float : ").split(","))]
    if panjang(data)>20:
        data=data[:20]
    return data
def bacaTabelChar():
    data=[x for x in input("Tabel Char : ").split(",")]
    if panjang(data)>20:
        data=data[:20]
    return data
def tulisTabelData(data):
    l=panjang(data)
    if l<1:
        print("{}")
    else:
        print("{",end="")
        for i in data:
            if 0<l-1:
                print(str(i)+"|",end="")
            else:
                print(i,end="")
            l-=1
        print("}")
def cariElm(data,elm):
    found=None
    for i in data:
        if i==elm:
            found=i
            break
    return found
def cariIdx(data,elm):
    found=None
    for i in range(panjang(data)):
        if data[i]==elm:
            found=i
            break
    return found
def cariBool(data,elm):
    found=False
    for i in data:
        if i==elm:
            found=True
            break
    return found
