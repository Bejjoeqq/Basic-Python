def main():
    maxx=-999999999999
    minn=999999999999
    while True:
        n=int(input("Input Nilai : "))
        if n>maxx:
            if n!=-99:
                maxx=n
        if n<minn:
            if n!=-99:
                minn=n
        if n==-99:
            break
        print("--->{}".format(n))
    print("Nilai Max = {}".format(maxx))
    print("Nilai Min = {}".format(minn))
if __name__ == '__main__':
    main()
