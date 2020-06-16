def panjang(data):
    count=0
    if data==None:
        return count
    else:
        for i in data:
            count+=1
    return count

def BacaTabelInt():
    data=[0]*int(input("Panjang Tabel Int : "))
    if panjang(data)>20:
        data=data[:20]
    return data

def BacaTabelFloat():
    data=[0.0]*int(input("Panjang Tabel Float : "))
    if panjang(data)>20:
        data=data[:20]
    return data

def BacaTabelChar():
    data=["0"]*int(input("Panjang Tabel Char : "))
    if panjang(data)>20:
        data=data[:20]
    return data

def TulisTabelData(data):
    if panjang(data)<1:
        print("{}")
    else:
        print("{",end="")
        for i in data:
            print(i,",",end="")
        print("}")

def CariElm(data,elm):
    found=None
    for i in data:
        if i==elm:
            found=i
            break
    return found

def CariIdx(data,elm):
    found=None
    for i in range(panjang(data)):
        if data[i]==elm:
            found=i
            break
    return found

def CariBool(data,elm):
    found=False
    for i in data:
        if i==elm:
            found=True
            break
    return found
