import random
def BubbleSort(A):
    n=0
    inc=0
    sum=0
    B=list()
    for x in A:
        n+=1
    swap = False
    while not swap:
        swap = True
        for i in range(1, n):
            if A[i-1]<A[i]:
                swap = False
                temp = A[i]
                A[i] = A[i-1]
                A[i-1] = temp
            else:
                pass

    for x in A:
        if x%2==0:
            B.append(x)
    return B,sum,inc
def main():
    data=[x for x in map(int, input("Tabel Int : ").split(","))]
    data,jumlah,banyak = BubbleSort(data)
    print(data)
    print("Banyak bilangan genap : ",banyak)
    print("Jumlah bilangan genap : ",jumlah)
if __name__ == '__main__':
    main()
