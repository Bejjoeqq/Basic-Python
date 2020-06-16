from tanggal import *
def main():
	#BacaTanggal()
	print("{}/{}/{} is Valid        	: {}".format(T["hari"],T["bulan"],T["tahun"],IsValidT(T["hari"],T["bulan"],T["tahun"])))
	print("{} is Kabisat          	 	: {}".format(T["tahun"],IsKabisat(T["tahun"])))
	print("{}/{}/{} getHari()       	: {}".format(T["hari"],T["bulan"],T["tahun"],getHari(T)))
	print("{}/{}/{} getBulan()      	: {}".format(T["hari"],T["bulan"],T["tahun"],getBulan(T)))
	print("{}/{}/{} getTahun()      	: {}".format(T["hari"],T["bulan"],T["tahun"],getTahun(T)))
	print("Print Tanggal 			  	: {}".format(TulisTanggal(T)))
	ResetTanggal()
	print("Reset tanggal 			  	: {}/{}/{}".format(T["hari"],T["bulan"],T["tahun"]))
	hh,bb,tt=BacaTanggal()
	PrevDay(T)
	print("Prev Day {}/{}/{}			: {}/{}/{}".format(hh,bb,tt,T["hari"],T["bulan"],T["tahun"]))
	hh,bb,tt=BacaTanggal()
	NextDay(T)
	print("Next Day {}/{}/{}			: {}/{}/{}".format(hh,bb,tt,T["hari"],T["bulan"],T["tahun"]))
	#print("Next Day {}/{}/{}			: {}/{}/{}".format())
	hh,bb,tt=BacaTanggal()
	NextNDay(T,15)
	print("Next 15 Day {}/{}/{}			: {}/{}/{}".format(hh,bb,tt,T["hari"],T["bulan"],T["tahun"]))
	hh,bb,tt=BacaTanggal()
	PrevNDay(T,15)
	print("Prev 15 Day {}/{}/{}		: {}/{}/{}".format(hh,bb,tt,T["hari"],T["bulan"],T["tahun"]))
	print("Tanggal {}/{}/{} Hari ke	: {}".format(T["hari"],T["bulan"],T["tahun"],HariKe(T)))
	T1={
		"hari":T["hari"],
		"bulan":T["bulan"],
		"tahun":T["tahun"]
	}
	hh,bb,tt=BacaTanggal()
	print(T1)
	print(T)
	print("IsEqD T dan T1				? {}".format(IsEqD(T1,T)))
	print("IsBefore T dan T1			? {}".format(IsBefore(T1,T)))
	print("IsAfter T dan T1			? {}".format(IsAfter(T1,T)))
	print("Hari bulan {}/{}			? {}".format(T["bulan"],T["tahun"],DayofMonth(T["bulan"],T["tahun"])))



if __name__ == "__main__":
	main()
