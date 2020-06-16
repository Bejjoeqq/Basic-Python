def main():
    f=0
    text=""
    print("C --> F")
    for x in range(-40,101):
        f=(x*(9/5))+32
        if x>=100:
            text="Air Mendidih"
        elif x>=40:
            text="Air Mandi Panas"
        elif x>=37:
            text="Temperatur Tubuh"
        elif x>=30:
            text="Cuaca Pantai"
        elif x>=21:
            text="Temperatur Ruangan"
        elif x>=10:
            text="Hari Yang Dingin"
        elif x>=0:
            text="Titik Beku Air"
        elif x>=-18:
            text="Cuaca Dingin Bersalju"
        elif x>=-40:
            text="Cuaca Sangat Dingin Bersalju"
        print("{:.0f} --> {:.2f} {}".format(x,f,text))
        text=""
if __name__ == '__main__':
    main()
