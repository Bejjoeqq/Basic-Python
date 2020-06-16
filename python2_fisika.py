import os
def cls():
    if os.name=="nt":
        os.system("cls")
    else:
        os.system("clear")
def biodata():
    print("INPUT APAPUN PROGRAM TIDAK AKAN ERROR!!!, NO BUG!!!")
    print("***************************")
    print("* Nama  = Aldhiya Rozak   *")
    print("* NIM   = A11.2019.12167  *")
    print("* Kelas = 4113            *")
    print("***************************")
def operatoraritmatika(bils,simbols):
    simbols=[0]
    simbols.clear()
    simbols=[0]
    for x in range(len(bils)):
        if bils[x]>=0:
            simbols[x]="+"
        else:
            simbols[x]=""
        simbols.append(x)
    return bils,simbols
def main():
    t="YES"
    simbols=[0]
    biodata()
    while True:
        if t=="YES" or t=="Y":
            try:
                cls()
                print("1. Menghitung Kecepatan Rata-Rata")
                print("2. Menghitung Kecepatan Sesaat")
                print("3. Menghitung Kelajuan Rata-Rata")
                n=float(input("Pilih Program (1-3) : "))
                if n==1:
                    print("\nRumus :       ∆r")
                    print("         ⊽ = ━━━━")
                    print("              ∆t")
                    print("\nPada Garis Lurus Kecepatan Rata-Rata")
                    print("ex input: (1,2)")
                    r=list(map(int,  input("Titik Awal, Titik Akhir (m) = ").split(',')))
                    t=list(map(int,  input("Waktu Awal, Waktu Akhir (s) = ").split(',')))
                    print("Diketahui : r1={}; r2={}; t1={}; t2={}".format(r[0],r[1],t[0],t[1]))
                    v=(r[1]-r[0])/abs(abs(t[1])-abs(t[0]))
                    print("Hasil : ⊽={}m/s\n".format(v))
                elif n==2:
                    print("\nRumus :       ds")
                    print("         v = ━━━━")
                    print("              dt")
                    print("\nPada Persamaan S(t)=at^2+bt+c")
                    print("ex input: (1,2,3)")
                    r1=list(map(int,  input("a, b, c = ").split(',')))
                    t1=abs(int(input("Kecepatan Benda Pada Saat (s) = ")))
                    rr1=r1[0]*2
                    v1=(rr1*t1)+r1[1]
                    r1, simbols = operatoraritmatika(r1,simbols)
                    print("Diketahui : Persamaan S(t)={}t^2{}{}t{}{} ".format(r1[0],simbols[1],r1[1],simbols[2],r1[2]))
                    print("Hasil : v={}({}){}{}".format(rr1,t1,simbols[1],r1[1]))
                    print("        v={}m/s".format(v1))
                elif n==3:
                    print("\nRumus :       s")
                    print("         v = ━━━")
                    print("              t")
                    print("\nPada Garis Lurus Kelajuan Rata-Rata")
                    print("ex input: (1,2)")
                    s=list(map(int,  input("Titik Awal, Titik Akhir (m) = ").split(',')))
                    tt=list(map(int,  input("Waktu Awal, Waktu Akhir (s) = ").split(',')))
                    print("Diketahui : s1={}; s2={}; t1={}; t2={}".format(s[0],s[1],tt[0],tt[1]))
                    vv=(s[1]-s[0])/abs(abs(tt[1])-abs(tt[0]))
                    print("Hasil : v={}m/s\n".format(vv))
                else:
                    print("Program hanya 1-3")

            except:
                print("INPUT HARUS ANGKA YANG BENAR")
        elif t=="NO" or t=="N":
            cls()
            print("See You Next Time")
            break
        else:
            print("Silahkan masukkan yes/y atau no/n")
        t=input("Apakah Ingin Melanjutkan? (YES/NO) : ").upper()
if __name__ == '__main__':
    main()
