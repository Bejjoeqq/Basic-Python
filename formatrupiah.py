def formatrupiah(uang):
    y = str(uang)
    if len(y) <= 3 :
        return 'Rp. ' + y
    else :
        p = y[-3:]
        q = y[:-3]
        return formatrupiah(q) + ',' + p
print(formatrupiah(int(input("Jumlah : "))))
