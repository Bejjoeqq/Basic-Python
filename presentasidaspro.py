def biod():
	print(">>>>> Nama   : Sekar Nabila A <<<<<")
	print(">>>>> NIM    : A11.2019.12155 <<<<<")
	print(">>>>> Kelas  :      4113      <<<<<")
	print("\n\t....PRESENTASI DASPRO....")



def main():
	biod()
	print("\n\t~~~~Selamat Datang di Penyetan Bejjo~~~~")
	print("Menu\n1.Ayam Penyet @10k \n2.Bebek Penyet @12k \n3.Ikan Penyet @9k \n4.Tempe Penyet @5k \n5.Tahu Penyet @5k \n6.Telur Penyet @5k \n7.Es Teh @4k \n8.Es Jeruk @5k \n8.Es Kopi @6k ")
	note=input("Apakah anda sudah mempunyai member [y/n] : ").upper()
	diskon=0
	totalkeseluruhan=0
	totalpesanan=""
	diskonpesan=""
	if note=="Y":
		kode=input("masukkan kode vocher anda =")
		if kode=="makanbanyak":
			diskon=10/100
			diskonpesan="Diskon 10%"
			print("Diskon 10% berhasil")
		elif kode=="bilandut":
			diskon=50/100
			diskonpesan="Diskon 50%"
			print("Woww potongan kamu 50%")
		else:
			print("Kode salah")

	elif note=="N":
		pass
	else:
		print("Input salah masukkan [Y/y] atau [N/n]")
	while True:
		menu=input("\nSilahkan pilih pesanan anda (1-8) : ")
		if menu=="1":
				harga=10000
				makanan = "Ayam Penyet"
				jumlah=int(input("masukkan jumlah {}=>".format(makanan)))
				totalharga=harga*jumlah
				totalkeseluruhan=totalkeseluruhan+(harga*jumlah)
				pesanan = "{} x {} = Rp{} ".format(makanan,jumlah,totalharga)
				print(pesanan)
				totalpesanan=totalpesanan+pesanan+"\n"
		elif menu=="2":
				harga=12000
				makanan = "Bebek Penyet"
				jumlah=int(input("masukkan jumlah {}=>".format(makanan)))
				totalharga=harga*jumlah
				totalkeseluruhan=totalkeseluruhan+(harga*jumlah)
				pesanan = "{} x {} = Rp{} ".format(makanan,jumlah,totalharga)
				print(pesanan)
				totalpesanan=totalpesanan+pesanan+"\n"
		elif menu=="3":
				harga=9000
				makanan = "Ikan Penyet"
				jumlah=int(input("masukkan jumlah {}=>".format(makanan)))
				totalharga=harga*jumlah
				totalkeseluruhan=totalkeseluruhan+(harga*jumlah)
				pesanan = "{} x {} = Rp{} ".format(makanan,jumlah,totalharga)
				print(pesanan)
				totalpesanan=totalpesanan+pesanan+"\n"
		elif menu=="4":
				harga=5000
				makanan = "Tempe Penyet"
				jumlah=int(input("masukkan jumlah {}=>".format(makanan)))
				totalharga=harga*jumlah
				totalkeseluruhan=totalkeseluruhan+(harga*jumlah)
				pesanan = "{} x {} = Rp{} ".format(makanan,jumlah,totalharga)
				print(pesanan)
				totalpesanan=totalpesanan+pesanan+"\n"
		elif menu=="5":
				harga=5000
				makanan = "Tahu Penyet"
				jumlah=int(input("masukkan jumlah {}=>".format(makanan)))
				totalharga=harga*jumlah
				totalkeseluruhan=totalkeseluruhan+(harga*jumlah)
				pesanan = "{} x {} = Rp{} ".format(makanan,jumlah,totalharga)
				print(pesanan)
				totalpesanan=totalpesanan+pesanan+"\n"
		elif menu=="6":
				harga=5000
				makanan = "Telur Penyet"
				jumlah=int(input("masukkan jumlah {}=>".format(makanan)))
				totalharga=harga*jumlah
				totalkeseluruhan=totalkeseluruhan+(harga*jumlah)
				pesanan = "{} x {} = Rp{} ".format(makanan,jumlah,totalharga)
				print(pesanan)
				totalpesanan=totalpesanan+pesanan+"\n"
		elif menu=="7":
				harga=4000
				minuman = "Es Teh"
				jumlah=int(input("masukkan jumlah {}=>".format(minuman)))
				totalharga=harga*jumlah
				totalkeseluruhan=totalkeseluruhan+(harga*jumlah)
				pesanan = "{} x {} = Rp{} ".format(makanan,jumlah,totalharga)
				print(pesanan)
				totalpesanan=totalpesanan+pesanan+"\n"
		elif menu=="8":
				harga=5000
				minuman = "Es Jeruk"
				jumlah=int(input("masukkan jumlah {}=>".format(minuman)))
				totalharga=harga*jumlah
				totalkeseluruhan=totalkeseluruhan+(harga*jumlah)
				pesanan = "{} x {} = Rp{} ".format(makanan,jumlah,totalharga)
				print(pesanan)
				totalpesanan=totalpesanan+pesanan+"\n"
		elif menu=="9":
				harga=6000
				minuman = "Es Kopi"
				jumlah=int(input("masukkan jumlah {}=>".format(minuman)))
				totalharga=harga*jumlah
				totalkeseluruhan=totalkeseluruhan+(harga*jumlah)
				pesanan = "{} x {} = Rp{} ".format(makanan,jumlah,totalharga)
				print(pesanan)
				totalpesanan=totalpesanan+pesanan+"\n"
		n=input("Apakah anda ingin memesan yang lain [y/n] : ").upper()
		if n=="N":
			print("\nTotal pesanan anda : ")
			print(totalpesanan)
			potongan=totalkeseluruhan*diskon
			totalsudahdidiskon=totalkeseluruhan-potongan
			print(diskonpesan)
			print("Jumlah yang harus dibayar Rp{} dipotong diskon Rp{} adalah Rp{}".format(totalkeseluruhan,int(potongan),int(totalsudahdidiskon)))
			while  True:
				bayar=int(input("Masukkan uang anda : "))
				kembalian = bayar - totalsudahdidiskon
				if kembalian<0:
					print("Uang anda kurang!")
				elif kembalian==0:
					print("Terima kasih uang anda pas")
					break
				else:
					print("Terima kasih kembalian anda Rp{}".format(int(kembalian)))
					break
			break
		elif n=="Y":
			pass
		else:
			print("Input salah masukkan [Y/y] atau [N/n]")
if __name__ == '__main__':
	main()
