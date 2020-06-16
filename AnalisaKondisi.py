def nomor1():
    n=list(map(int, input("Masukkan 3 nilai integer : ").split(",")))
    sums=0
    nn=10
    for x in range(len(n)):
        if n[x]==13:
            nn=x
            break
    if nn==0:
        sums=0
    elif nn==1:
        sums=n[0]
    elif nn==2:
        sums=n[0]+n[1]
    else:
        sums=n[0]+n[1]+n[2]
    print(sums)
def nomor2():
    n=list(map(int, input("Masukkan 3 nilai integer : ").split(",")))
    sums=0
    if n[0]==n[1] and n[1]==n[2]:
        sums=0
    elif n[0]==n[1]:
        sums=n[2]
    elif n[1]==n[2]:
        sums=n[0]
    elif n[2]==n[0]:
        sums=n[1]
    else:
        sums=n[0]+n[1]+n[2]
    print(sums)
def nomor3():
    n=list(map(int, input("Masukkan 3 nilai integer : ").split(",")))
    c=abs(n[0]-n[1])
    b=abs(n[0]-n[2])
    if c>=2 or b>=2:
        if abs(n[1]-n[2])>=2:
            print("True")
        else:
            print("False")
    else:
        print("False")


def main():
    nomor3()

if __name__ == '__main__':
    main()
