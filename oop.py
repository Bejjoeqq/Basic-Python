hargaBeras=[14000,125000,13000,10000,11000,11000,9750]
kunjunganHarian=[500,400,300,340,557,200,900]

class hargabahanpokokPasar:
    global hargaBeras,kunjunganHarian
    def _init_(self,p,s):
        self.harga=p
        self.jumlah=s

    def mean(self):
        for i in range(self.harga):
            i=self.harga
        for j in range(self.jumlah):
            j=self.jumlah
        rumus=len(a+b)/2

    def median(self):
        self.harga.sort()
        if len(self.harga) % 2==0:
            convertInt=int(len(self.harga)/2)
            rumusMedian=(self.harga[a-1]+self.harga[a])/2
        else:
            convertInt=int((len(self.harga)+1)/2)
            rumusMedian=self.harga[a-1]
        print("Median Harga Beras\t:{}".format(rumusMedian))

    def modus(self,x=[]):
        agt=set(x)
        simpan=[]
        nilaiTertinggi=0
        for j in agt:
            jum=x.count(j)
            if(jum>1 and jum>nilaiTertinggi):
                simpan.clear()
                nilaiTertinggi=jum
                simpan.append(j)
            elif(jum==nilaiTertinggi):
                simpan.append(j)
        return simpan
        print("Modus Harga Beras\t:{}".format(simpan(self.harga)))

    def standarDeviasi(self):
        standarD=np.std(self.harga)
        print("Standar Deviasi Harga Beras\t:{}".format(standarD))

    def kuartil(self):
        q1=np.quantile(self.harga,0.25)
        q2=np.quantile(self.harga,0.5)
        q3=np.quantile(self.harga,0.75)
        print("Kuartil 1 Harga Beras\t:{}".format(q1))
        print("Kuartil 2 Harga Beras\t:{}".format(q2))
        print("Kuartil 3 Harga Beras\t:{}".format(q3))

    def kovarianHarganJumlah(self):
        dataJadi=np.array([self.harga,self.jumlah])
        hasilKov=np.cov(dataJadi)
        print("Kovarian Harga Beras dengan Jumlah Kunjungan\t:{}".format(hasilKov))

    def korelasiHarganJumlah(self):
        dataJadi=np.array([self.harga,self.jumlah])
        hasilKor=np.corrcoef(dataJadi)
        print("Korelasi Harga Beras dengan Jumlah Kunjungan\t:{}".format(hasilKor))

print("===============Menghitung Harga Beras===================")
pantauan=hargabahanpokokPasar(hargaBeras,kunjunganHarian)
print(hargaBeras)
print(kunjunganHarian)
pantauan.mean()
pantauan.median()
pantauan.modus()
pantauan.standarDeviasi()
pantauan.kuartil()
pantauan.kovarianHarganJumlah()
pantauan.korelasiHarganJumlah()
