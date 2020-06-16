def main():
    xy=0
    while True:
        n=int(input("Input Nilai : "))
        if n!=9999:
            xy+=1
        if n==9999:
            break
        print("--->{}".format(n))
    print("Jumlah = {}".format(xy))
if __name__ == '__main__':
    main()
