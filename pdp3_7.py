def main():
	n=int(input()) 

	if((n>3) and (n<10)):      
		benar=True 
	else:     
		benar=False
	print("3<{}<10 adalah {}\n".format(n,benar))

	if (n>=5) and (n<=6):
		benar=True
	else:
		benar=False
	print("5<={}<=6 adalah {}\n".format(n,benar))

	if ((n>=5) and (n<=6)) or n>=10:
		benar=True
	else:
		benar=False
	print("5<={}<=6 atau {}>=10 adalah {}\n".format(n,n,benar))

	if (n>=3) and (n<=7):
		benar=True
	else:
		benar=False
	print("interval(3,7) : {} adalah {}\n".format(n,benar))

	if (n>=3) and (n<=15):
		benar=True
	else:
		benar=False
	print("interval(3,15) : {} adalah {}\n".format(n,benar))

	if (n>=5) and (n<25):
		benar=True
	else:
		benar=False
	print("interval(5,24) : {} adalah {}\n".format(n,benar))

	if ((n>=3) and (n<=15)) or ((n>=22) and (n<=32)):
		benar=True
	else:
		benar=False
	print("interval(3,15) atau (22,32) : {} adalah {}\n".format(n,benar))

	if ((n>=2) and (n<=5)) or ((n>=15) and (n<=27)):
		benar=True
	else:
		benar=False
	print("interval(2,5) atau (15,27) : {} adalah {}\n".format(n,benar))

	if (n<5) or (n>17):
		benar=True
	else:
		benar=False
	print("n<5 atau n>17 : {} adalah {}\n".format(n,benar))

	if (n<8) or ((n>=9) and (n<=15)) or ((n>=21) and (n<=33)):
		benar=True
	else:
		benar=False
	print("n<8 atau interval(9,15) atau interval(21,33) : {} adalah {}\n".format(n,benar))

	if (n<8) or ((n>=9) and (n<=15)) or ((n>=21) and (n<=30)) or n>34:
		benar=True
	else:
		benar=False
	print("n<8 atau interval(9,15) atau interval(21,30) : {} adalah {}\n".format(n,benar))
if __name__=='__main__':
	main()