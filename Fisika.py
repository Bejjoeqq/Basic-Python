import time
def biod():
	print("\n***************************")
	print("* Nama  = Aldhiya Rozak   *")
	print("* NIM   = A11.2019.12167  *")
	print("* Kelas = 4113            *")
	print("***************************")
def operatorarit(bils,simbols):
	simbols=[0]
	simbols.clear()
	simbols=[0]
	for x in range(len(bils)):
		if bils[x]>=0:
			simbols[x]="+"
		else:
			simbols[x]=""
		simbols.append(x)
	return bils,simbols

def plusnmin():
	simbol=[0]
	print("\n(format  : xi,yj,zk)\n(example : 1,2,3)")
	bil1=list(map(int,  input("Masukkan Vektor a = ").split(',')))
	bil2=list(map(int,  input("Masukkan Vektor b = ").split(',')))

	bil1, simbol = operatorarit(bil1,simbol)
	print("\nDiketahui : Va = ({}i{}{}j{}{}k)".format(bil1[0],simbol[1],bil1[1],simbol[2],bil1[2]))

	bil2, simbol = operatorarit(bil2,simbol)
	print("            Vb = ({}i{}{}j{}{}k)".format(bil2[0],simbol[1],bil2[1],simbol[2],bil2[2]))

	print("\nDitanya : a. Va + Vb")
	print("          b. Va - Vb")

	jmlh=[0,0,0]
	for x in range(len(jmlh)):
		jmlh[x]=bil1[x]+bil2[x]

	kurng=[0,0,0]
	for x in range(len(kurng)):
		kurng[x]=bil1[x]-bil2[x]

	jmlh, simbol = operatorarit(jmlh,simbol)
	print("\nHasil : a. {}i{}{}j{}{}k".format(jmlh[0],simbol[1],jmlh[1],simbol[2],jmlh[2]))

	kurng, simbol = operatorarit(kurng,simbol)
	print("        b. {}i{}{}j{}{}k".format(kurng[0],simbol[1],kurng[1],simbol[2],kurng[2]))
	input("Enter...")

def SkalarV():
	simbol=[0]
	print("\n(format  : xi,yj,zk)\n(example : 1,2,3)")
	bil3=list(map(int,  input("Masukkan Vektor a = ").split(',')))
	sklr=int(input("Masukkan Skalar = "))

	bil3, simbol = operatorarit(bil3,simbol)
	print("\nDiketahui : Va = ({}i{}{}j{}{}k)".format(bil3[0],simbol[1],bil3[1],simbol[2],bil3[2]))
	print("\nDitanya : Va . k")

	kali=[0,0,0]
	for x in range(len(kali)):
		kali[x]=bil3[x]*sklr

	kali, simbol = operatorarit(kali,simbol)
	print("\nHasil : {}i{}{}j{}{}k".format(kali[0],simbol[1],kali[1],simbol[2],kali[2]))
	input("Enter...")

def latihn():
	print("\n1. Vp = (15i+14j-16k)")
	print("   Va = (18i-25j+24k)")

	i1,j1,k1,i2,j2,k2=15,14,-16,18,-25,24

	ti=i1+i2
	tj=j1+j2
	tk=k1+k2

	ki=i1-i2
	kj=j1-j2
	kk=k1-k2

	print("\n   a. Vp + Va = {}i{}j+{}k".format(ti,tj,tk))
	print("   b. Vp - Va = {}i+{}j{}k".format(ki,kj,kk))

	print("\n2. m = 100kg")
	print("   v = (15i+60j-2k)m/s")

	i3,j3,k3,m=15,60,-2,100

	ii=i3*m
	jj=j3*m
	kk=k3*m

	print("\n   m . v = {}i+{}j{}k".format(ii,jj,kk))
	input("Enter...")
def main():
	biod()
	i = 1
	while i < 69:
		print("\n1. Penjumlahan & Pengurangan Vektor")
		print("2. Perkalian Skalar Vektor")
		print("3. Latihan Soal Di Papan Tulis")
		print("4. Exit")
		a = input("Pilih Program(1-4) : ")
		if a == "1":
			plusnmin()
		elif a == "2":
			SkalarV()
		elif a == "3":
			latihn()
		elif a == "4":
			print("Thank You")
			break
		else :
			print("Salah Input, Silahkan Input 1-4")
			input("Enter...")
		i+=1
if __name__=='__main__':
	main()
