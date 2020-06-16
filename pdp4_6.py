def main():
    a=int(input("Masukkan Nilai Angka : "))
    if a>80:
        text="A"
    elif a>=61:
        text="B"
    elif a>=41:
        text="C"
    elif a>=21:
        text="D"
    elif a>=0:
        text="E"
    else:
        text="Tidak Boleh Negatif"
    print("Nilai : {}, Bobot : {}".format(a, text))
if __name__ == '__main__':
    main()
