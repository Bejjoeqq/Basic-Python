from arrayList import *

# data1=[2,42,32,12,22,39,15,8,4,20]
# data2=[3.45,2.33,1.49,4.00,3.86,3.92,3.21,2.89,2.45,2.68]
# data3=['A','G','U','S','-','W','A','H','Y','U']

data1=bacaTabelInt()#2,42,32,12,22,39,15,8,4,20
data2=bacaTabelFloat()#3.45,2.33,1.49,4.00,3.86,3.92,3.21,2.89,2.45,2.68
data3=bacaTabelChar()#A,G,U,S,-,W,A,H,Y,U

def main():
    print("data1: ",end='');tulisTabelData(data1)
    print("data2: ",end='');tulisTabelData(data2)
    print("data3: ",end='');tulisTabelData(data3)
    print("Cari      22  : {}".format(cariElm(data1,22)))
    print("Cari idx  22  : {}".format(cariIdx(data1,22)))
    print("Cari Bool 22  : {}".format(cariBool(data1,22)))
    print("Cari     3.86 : {}".format(cariElm(data2,3.86)))
    print("Cari idx 3.86 : {}".format(cariIdx(data2,3.86)))
    print("Cari Bool 3.86: {}".format(cariBool(data2,3.86)))
    print("Cari      'W' : {}".format(cariElm(data3,'W')))
    print("Cari idx  'W' : {}".format(cariIdx(data3,'W')))
    print("Cari Bool 'W' : {}".format(cariBool(data3,'W')))

    print("Ta da ! ")


if __name__ == '__main__':
    main()
