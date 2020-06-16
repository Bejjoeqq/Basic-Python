from sys import argv
def main():
	#2.5,5
	l=list(map(float,  argv[1].split(",")))
	a=l[0]
	l=0.5*l[0]*l[0]
	print("luas segitiga alas {} dan tinggi {} adalah : {}".format(a,a,l))
if __name__=='__main__':
	main()
