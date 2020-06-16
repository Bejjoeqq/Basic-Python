from sys import argv
def main():
	#23.5
	r=list(map(float,  argv[1].split(',')))
	jari=r[0]
	r=3.14*r[0]*r[0]
	print("luas lingkarang jari-jari {} adalah : {}".format(jari,r))
if __name__=='__main__':
	main()



