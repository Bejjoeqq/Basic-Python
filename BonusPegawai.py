def formatrupiah(uang):
    y = str(uang)
    if len(y) <= 3 :
        return 'Rp. ' + y
    else :
        p = y[-3:]
        q = y[:-3]
        return formatrupiah(q) + ',' + p
        print('Rp. ' +  formatrupiah(q) + ',' + p)
def main():
    bonus=0
    staff=int(input("Pegawai(1)/Non Pegawai(0) : "))
    mk=int(input("Masa Kerja Anda : "))
    umur=int(input("Umur Anda : "))
    if staff==1:
        if mk>=5 and umur>=50:
            bonus=1000000
        elif mk<5:
            bonus=500000
        if umur<50:
            bonus=bonus+300000
    elif staff==0:
        if mk>=5 and umur>=50:
            bonus=400000
        else:
            bonus=250000

    bonus = formatrupiah(bonus)
    print(bonus)
if __name__ == '__main__':
    main()
