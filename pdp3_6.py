def f1(p,q):
	r1=p and q
	return r1
def f2(p,q):
	r2= not (p and q)
	return r2
def f3(p):
	r3= not p
	return r3
def f4(q):
	r4= not q
	return r4
def f5(p,q):
	r5= p or (not q)
	return r5
def f6(p,q):
	r6= not (p and q)
	return r6
def f7(p,q):
	r7= not (p or q)
	return r7
def f8(p,q):
	if p==q:
		r8=False
	else:
		r8=True
	return r8
def f9(p,q):
	if p==q:
		r9=True
	else:
		r9=False
	return r9
def output(h):
	print("T : T = {}".format(h[0]))
	print("T : F = {}".format(h[1]))
	print("F : T = {}".format(h[2]))
	print("F : F = {}".format(h[3]))
def main():
	andv1=[0,0,0,0]
	andv2=[0,0,0,0]
	andv3=[0,0,0,0]
	andv4=[0,0,0,0]
	andv5=[0,0,0,0]
	andv6=[0,0,0,0]
	andv7=[0,0,0,0]
	andv8=[0,0,0,0]
	andv9=[0,0,0,0]
	tf1=[True,True,False,False]
	tf2=[True,False,True,False]
	for x in range(0,4):
		andv1[x] = f1(tf1[x],tf2[x])
		andv2[x] = f2(tf1[x],tf2[x])
		andv3[x] = f3(tf1[x])
		andv4[x] = f4(tf2[x])
		andv5[x] = f5(tf1[x],tf2[x])
		andv6[x] = f6(tf1[x],tf2[x])
		andv7[x] = f7(tf1[x],tf2[x])
		andv8[x] = f8(tf1[x],tf2[x])
		andv9[x] = f9(tf1[x],tf2[x])
	print("Output 1 :")
	output(andv1)
	print("\nOutput 2 :")
	output(andv2)
	print("\nOutput 3 :")
	output(andv3)
	print("\nOutput 4 :")
	output(andv4)
	print("\nOutput 5 :")
	output(andv5)
	print("\nOutput 6 :")
	output(andv6)
	print("\nOutput 7 :")
	output(andv7)
	print("\nOutput 8 :")
	output(andv8)
	print("\nOutput 9 :")
	output(andv9)
if __name__=='__main__':
	main()