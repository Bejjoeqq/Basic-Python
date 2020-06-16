from sys import argv
def main():
	#7.5,8.3
	l=list(map(float,  argv[1].split(",")))
	a=l[0]
	b=l[1]
	c=a*b
	print("luas persegi {} X {} = {}".format(a,b,c))
if __name__=='__main__':
	main()