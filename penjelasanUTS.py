import math
def main():
    n=20
    m=30
    nm=0
    awal=0
    for j in range(n,m+1):
        awal=j
        i=1
        sum=0
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n{}".format(j))
        print("Range : {} - {}".format(i, int(math.sqrt(j))))
        for i in range(1,int(math.sqrt(j)+1)):
            print("\n{}".format(i))
            print("if {}%{}==0".format(j, i))
            if j%i==0:
                print("-->")
                print("if {}=={}".format(j/i, i))
                if (j/i==i):
                    print("-->")
                    sum=sum+i
                    print("true : {}<={}".format(sum,i))
                else:
                    print("#")
                    nm=sum
                    sum=sum+i
                    print("false : {}<={}+{}".format(sum,nm,i))
                    nm=sum
                    sum=sum+(j/i)
                    print("false : {}<={}+({}/{})".format(sum,nm,j,i))
            else:
                print("#")
        nm=sum
        sum=sum-j
        print("\nsum = {}-{}".format(nm,j))
        print("sum = {}".format(sum))
        print("{}<{}".format(sum, j))
        if (sum<j):
            print("\n{} = Y".format(awal))
        else:
            print("\n{} = T".format(awal))

        print("\n")
if __name__ == '__main__':
    main()
