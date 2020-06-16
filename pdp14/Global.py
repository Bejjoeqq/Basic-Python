from mesinkarakter import *
def main():
	global CC
	print("Mulai Awal Pita...")
	CC=START()
	print("{}".format(CC),end="")
	while (not EOP()):
		CC=ADV()
		print("{}".format(CC),end="")
	print("\nAkhir Pembacaan pita...\n")
	print("\nTest fungsi-fungsi...\n")
	print("Panjang File : {}".format(panjang()))
	print("Huruf Char not blank : {}".format(HitungCH()))
	l,u,o = HitungHuruf()
	print("low : {} , upper : {} , other : {}".format(l,u,o))
	print("Count A : {} ".format(Hitung_A()))
	print("Vokal : {} ".format(HitungVokal()))
	print("AN : {}".format(HitungAN()))
	print("Blank : {} ".format(HitungBlank()))

if __name__ == '__main__':
		main()
