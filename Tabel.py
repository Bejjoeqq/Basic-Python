nama=["Nama","Aldi","Joel","Bejjo","Aaaaaaaaaaa"]
porsi=["Porsi","5","2","4","40000000"]
harga=["Harga","500","200","400","400000000000"]
namalen=0;porsilen=0;hargalen=0
for x in nama:
    if len(x)>namalen:
        namalen=len(x)
for x in porsi:
    if len(x)>porsilen:
        porsilen=len(x)
for x in harga:
    if len(x)>hargalen:
        hargalen=len(x)
for x in range(len(nama)):
    a=namalen-len(nama[x])
    namaa=(" "*a)+nama[x]

    a=porsilen-len(porsi[x])
    porsii=(" "*a)+porsi[x]

    a=hargalen-len(harga[x])
    hargaa=(" "*a)+harga[x]

    print("[{}][{}][{}]".format(namaa,porsii,hargaa))
    if x==0:
        print("_"*(namalen+porsilen+hargalen+6))
