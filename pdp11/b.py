from a import *
data1=[2,42,32,12,22,39,15,8,4,20]
data2=[3.45,2.33,1.49,4.00,3.86,3.92,3.21,2.89,2.45,2.68]
data3=["A","G","U","S","-","W","A","H","Y","U"]
def main():
    print("data 1: ",end="");TulisTabelData(data1)
    print("data 2: ",end="");TulisTabelData(data2)
    print("data 3: ",end="");TulisTabelData(data3)
    print("Cari      22  : {}".format(CariElm(data1,22)))
    print("Cari idx  22  : {}".format(CariIdx(data1,22)))
    print("Cari Bool 22  : {}".format(CariBool(data1,22)))
    print("Cari     3.86 : {}".format(CariElm(data2,3.86)))
    print("Cari idx 3.86 : {}".format(CariIdx(data2,3.86)))
    print("Cari Bool 3.86: {}".format(CariBool(data2,3.86)))
    print("Cari       W : {}".format(CariElm(data3,"W")))
    print("Cari idx   W : {}".format(CariIdx(data3,"W")))
    print("Cari Bool  W : {}".format(CariBool(data3,"W")))
if __name__ == "__main__":  main()
