def main():
    sum=0
    while True:
        n=int(input("Input Nilai : "))
        if n!=9999:
            sum=sum+n
        if n==9999:
            break
        print("--->{}".format(n))
    print("Jumlahan = {}".format(sum))
if __name__ == '__main__':
    main()
