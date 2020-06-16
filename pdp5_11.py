def main():
    for x in range(1,11):
        for y in range(1,8):
            z=x*y
            print("{:>2} x {:>1} = {:>2}".format(x,y,z),end="     ")
        print("")
if __name__ == '__main__':
    main()
