def main():
    f=0
    print("C-->F")
    for x in range(0,101):
        f=(x*(9/5))+32
        print("{:.0f}-->{:.2f}".format(x,f))
if __name__ == '__main__':
    main()
