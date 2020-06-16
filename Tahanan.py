def main():
    a=int(input("1=Seri, 0=Paralel : "))
    r=list(map(int, input("Masukkan R1,R2,R3 : ").split(",")))
    if a==1:
        if r[0]>=0 and r[1]>=0 and r[2]>=0:
            rt=r[0]+r[1]+r[2]
            print("R Total = {}".format(rt))
        else:
            print("Tidak Boleh R<0")

    elif a==0:
        if r[0]!=0 and r[1]!=0 and r[2]!=0:
            rt=(r[0]*r[1]*r[2])/((r[0]*r[1])+(r[1]*r[2])+(r[2]*r[0]))
            print("R Total = {0:.2f}".format(rt))
        else:
            print("Tidak Boleh R=0")

    else:
        print("Input Salah")

if __name__ == '__main__':
    main()
