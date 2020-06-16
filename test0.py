def panjangData(data):
    count=0
    if data==None:
        return count
    else:
        for i in data:
            count+=1
    return count

def nilaiMutlak(n):
    if n<0:
        n*=-1
    else:
        n*=1
    return n

def geserArray(A,n):
    B = list()
    if nilaiMutlak(n)<=panjangData(A):
        for x in range(panjangData(A)):
            newIndex = x+n;
            if newIndex>=panjangData(A):
                newIndex-=panjangData(A)
            elif newIndex<0:
                newIndex+=panjangData(A)
            B.append(A[newIndex])
        if n<0:
            note="ke kiri"
        else:
            note="ke kanan"
    else:
        note="n melebihi jumlah index"
    return B,n,note

def main():
    A=[4,5,6,7,8,9,10]
    n=2
    # A=list(map(int, input("Array bilangan integer : ").split(",")));n=int(input("Geser array sebanyak : ")) #<--- enable this to make input
    Atemp=A
    A,n,note=geserArray(A,n)
    print("Array A : {}\nDigeser sebanyak {} {}\nHasil Array A : {}".format(Atemp,nilaiMutlak(n),note,A))
    print("reverseArray : ")
    print("")
if __name__ == '__main__':
    main()
