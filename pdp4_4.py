def main():
    print("Persamaan kuadrat ax^2+bx+c")
    a=list(map(int, input("Masukkan 3 integer : ").split(",")))
    d=(a[1]**2)-(4*a[0]*a[2])
    if d>0:
        print("Kuadrat mempunyai dua akar real = {}".format(d))
    elif d==0:
        print("Kuadrat sempurna maka kedua akarnya rasional = {}".format(d))
    elif d<0:
        print("Imajiner = {}".format(d))
if __name__ == '__main__':
    main()
