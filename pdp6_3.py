def main():
    n=int(input("Jumlah Analisa : "))
    y=0
    for x in range(1,n+1):
        print("{} + {} = ? ".format(x,x), end='')
        jawab=int(input())
        if jawab==x+x:
            print("Benar\n")
        else:
            print("Salah\nJawabannya adalah {}\n".format(x+x))
            y+=1
    print("Analisis : \nJumlah Analisa = {}\nAnalisa Benar = {}\nAnalisa Salah = {}".format(n,n-y,y))

if __name__ == '__main__':
    main()
