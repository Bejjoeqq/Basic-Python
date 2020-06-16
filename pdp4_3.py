def main():
    a=list(map(int, input().split(",")))
    if a[0]==a[1] or a[0]==a[2] or a[1]==a[2]:
        print("ADA")
    else:
        print("TIDAK ADA")

if __name__ == '__main__':
    main()
