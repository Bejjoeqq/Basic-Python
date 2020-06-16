import math
def chFirstLast(N):
    c=0
    Nn=N
    while True:
        Nn//=10
        c+=1
        if Nn==0:
            break
    c=c-1
    last = N % 10
    first = N // 10**c
    a = first * 10**c
    b = N % a
    num = b // 10
    hasil = (last * (10**c)) + (num*10) + first
    return hasil
def swapDigit(N):
    temp="";hasil=""
    while True:
        temp=N%10
        N//=10
        hasil+=str(temp)
        if N==0:
            break
    return hasil
def main():
    N=int(input("Bilang Integer : "))
    print("swapDigit : ",swapDigit(N))
    print("chFirstLast : ",chFirstLast(N))
if __name__ == '__main__':
    main()
