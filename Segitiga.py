def main():
    sisi=list(map(int, input("Masukkan 3 Sisi Segitiga : ").split(",")))
    if (sisi[0]+sisi[1])>sisi[2] and (sisi[0]+sisi[2])>sisi[1] and (sisi[1]+sisi[2])>sisi[0]:
        if ((sisi[0]**2)+(sisi[1]**2))==sisi[2]**2:
            print("Segitiga Siku-siku")
        elif ((sisi[0]**2)+(sisi[1]**2))>sisi[2]**2:
            print("Segitiga Lancip")
        elif ((sisi[0]**2)+(sisi[1]**2))<sisi[2]**2:
            print("Segitiga Tumpul")
    else:
        print("Tidak memungkinkan membentuk segitiga")
if __name__ == '__main__':
    main()
