import os
def cls():
    if os.name=="nt":
        os.system("cls")
    else:
        os.system("clear")
def main():
    t="YES"
    while True:
        if t=="YES" or t=="Y":
            try:
                cls()
                n=float(input("Input N>1 = "))
                n1=str(int(n))
                text=""
                nt=n
                if n>1:
                    while True:
                        if n!=1:
                            if n%2==0:
                                n=n/2
                            else:
                                n=(3*n)+1
                        elif n==1:
                            break
                        if n>nt:
                            nt=n
                        text=text+str(int(n))+" "
                    text=n1+" "+text
                    print(text)
                    print(int(nt))
                else:
                    print("Input harus bilangan lebih dari 1")
            except:
                print("INPUT HARUS ANGKA YANG BENAR")
        elif t=="NO" or t=="N":
            cls()
            print("Thank You")
            break
        else:
            print("Silahkan masukkan yes/y atau no/n")
        t=input("Apakah Ingin Melanjutkan? (YES/NO) : ").upper()
if __name__ == '__main__':
    main()
