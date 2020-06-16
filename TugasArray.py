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
    hasilList=list()
    if n<=0:
        for x in range(n,panjangData(A)+n):
            if nilaiMutlak(n)<=panjangData(A):
                hasilList.append(A[x])
            else:
                print("n melebihi jumlah index")
                break
        note="ke kiri"
        if n==0:
            note="(tetap)"
    else:
        for x in range(n,panjangData(A)):
            if nilaiMutlak(n)<panjangData(A):
                hasilList.append(A[x])
            else:
                print("n melebihi jumlah index")
                break
        for x in range(0,n):
            if nilaiMutlak(n)<panjangData(A):
                hasilList.append(A[x])
            else:
                print("n melebihi jumlah index")
                break
        note="ke kanan"
    return hasilList,n,note
def main():
    A=[4,5,6,7,8,9,10]
    n=0
    # A=list(map(int, input("Array bilangan integer : ").split(",")));n=int(input("Geser array sebanyak : ")) #<--- enable this to make input
    Atemp=A
    A,n,note=geserArray(A,n)
    print("Array A : {}\nDigeser sebanyak {} {}\nHasil Array A : {}".format(Atemp,nilaiMutlak(n),note,A))
if __name__ == '__main__':
    main()
