from sys import argv
def main():
	#5.5,2.3
	r=list(map(float,  argv[1].split(",")))
	PI=3.14
	a=r[0]
	b=r[1]
	L1=PI*r[0]*r[0]
	L2=PI*r[1]*r[1]
	sl=L1-L2
	print("Luas L1, r={} : {}".format(a,L1))
	print("Luas L2, r={} : {}".format(b,L2))
	print("Selisih L1-L2 : {}".format(sl))
if __name__=='__main__':
	main()