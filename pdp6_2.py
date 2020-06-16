import random
def main():
    while True:
        x = random.randint(1,50)
        y=0
        while True:
            y+=1
            n=int(input("Tebakan ke-{}, Masukan angka tebakan ? : ".format(y)))
            if n>x:
                print("Angka Anda Lebih Besar")
            elif n<x:
                print("Angka Anda Lebih Kecil")
            elif n==x:
                print("Hebat angka {} berhasil anda tebak dalam {} kali".format(x,y))
                break
            if y==5:
                print("Anda tidak berhasil menebak, angka ajaib = {}".format(x))
                break
        nn=input("Apakah anda akan bermain lagi [Yy/Tt] : ").upper()
        if nn=="T" or nn=="TT":
            print("Selamat tinggal")
            break
        print("\n")
if __name__ == '__main__':
    main()
