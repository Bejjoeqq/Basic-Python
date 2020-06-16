kilasUmurAnak={
    0:[21,15],
    1:[17,14],
    2:[30,21,5],
    3:[25,23,21,19],
    4:[17],
    5:[6,3],
    6:[1,12]
}
suspectUmurAtas=int(input("Suspect anak berumur (batas atas)\t"))
suspectUmurBawah=int(input("Suspect anak berumur (batas bawah)\t"))
suspectUrutan=int(input("Suspect anak lahiran ke-\t"))-1

def miripPolisi(keluarga):
    global suspectUrutan,suspectUmurBawah,suspectUmurAtas,kilasUmurAnak
    try:
        if kilasUmurAnak[keluarga][suspectUrutan]>suspectUmurBawah and kilasUmurAnak[keluarga][suspectUrutan]<suspectUmurAtas:
            print("dikeluarga ke-{}, anak lahiran ke-{} berumur: {}".format(keluarga+1,suspectUrutan+1,kilasUmurAnak[keluarga][suspectUrutan]))
        else:
            print("dikeluarga ke-{}, anak lahiran ke-{} tidak memenuhi kriteria tersangka".format(keluarga+1,suspectUrutan+1))
    except:
        print("[list index out of range] Pemilihan data keluarga untuk calon tersangka salah. Jumlah anak dalam keluarga ke-{} tidak sesuai.".format(keluarga+1))
for keluarga in range(len(kilasUmurAnak)):
    miripPolisi(keluarga)
