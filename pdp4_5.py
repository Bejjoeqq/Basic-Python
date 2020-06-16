def main():
    a=int(input("Masukkan Jumlah Boneka : "))
    if a>50:
        harga=10
    elif a>=11:
        harga=20
    elif a>=2:
        harga=25
    elif a==1:
        harga=30
    else:
        print("Tidak Boleh <=0 : ERROR")
        harga=0
    total=harga*a
    print(total)

if __name__ == '__main__':
    main()
