from sys import argv
def main():

	#35,23,76,45,50,10,15,25,4,17
	data=list(map(int,  argv[1].split(',')))

	for i in range(len(data)):
		data[i]=int(data[i])
		jmlh=0
	rata=jmlh/len(data)
	sigma=0

	for i in range(len(data)):
		hitung=(data[i]-rata)**2
		sigma += hitung
	pmbg=sigma/len(data)
	sd=pmbg**0.5

	print("Nilai Minimum = {}".format(min(data)))
	print("Nilai Maximum = "+str(max(data)))
	print("Nilai Rata-Rata = "+str(sum(data)/len(data)))
	print("Nilai Simpangan Baku = {}".format(sd))
if __name__=='__main__':
	main()
