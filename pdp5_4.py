def main():
    sum=0
    rt=0
    for x in range(1,21):
        sum=sum+x
        print(x)
    rt=sum/20
    print("Jumlah = {}".format(sum))
    print("Rata-rata = {}".format(rt))
if __name__ == '__main__':
    main()
