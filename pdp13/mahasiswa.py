from math import *
class mahasiswa():
	def __init__(self,nim=None,nama=None,ipk=0.0):
		self.nim=nim
		self.nama=nama
		self.ipk=ipk

def panjang(m):
	count=0
	for i in m:
		count=count+1
	return count

def isEmpty(m):
	if m==None or (nim==None and nama==None and ipk==0,0):
		return True

def setNim(m,newnim):
	mhs=mahasiswa()
	mhs.nim=newnim

def setNama(m,newnama):
	mhs=mahasiswa()
	mhs.nama=newnama

def setIpk(m,newipk):
	mhs=mahasiswa()
	mhs.ipk=newipk

def getNim(m):
	return m.nim

def getNama(m):
	return m.nama

def getIpk(m):
	return m.ipk

def BacaData():
	mhs=mahasiswa()
	mhs.nim,mhs.nama,ipkk=map(str, input("Baca Jam : ").split(","))
	mhs.ipk=float(ipkk)

def TulisData(m):
	if m!=None:
		mhs=mahasiswa()
		mhs.nim=m.nim
		mhs.nama=m.nama
		mhs.ipk=m.ipk
		print(mhs.nim,mhs.nama,mhs.ipk)
		print("")
	else:
		print("Tidak ada\n")


def printList(data):
	for elm in data:
		TulisData(elm)

def Sorting(m,idx):
	if idx==0:
		for i in range(panjang(m)-1):
			minus=i
			for j in range(i+1,panjang(m)):
				if m[j].nim<m[minus].nim:
					minus=j
			temp=m[i]
			m[i]=m[minus]
			m[minus]=temp
		print("Sort by nim : ")
		for x in range(panjang(m)):
			print(m[x].nim,m[x].nama,m[x].ipk)
		print("")
	elif idx==1:
		for i in range(panjang(m)-1):
			minus=i
			for j in range(i+1,panjang(m)):
				if m[j].nama<m[minus].nama:
					minus=j
			temp=m[i]
			m[i]=m[minus]
			m[minus]=temp
		print("Sort by nama : ")
		for x in range(panjang(m)):
			print(m[x].nama,m[x].nim,m[x].ipk)
		print("")
	elif idx==2:
		for i in range(panjang(m)-1):
			minus=i
			for j in range(i+1,panjang(m)):
				if m[j].ipk<m[minus].ipk:
					minus=j
			temp=m[i]
			m[i]=m[minus]
			m[minus]=temp
		print("Sort by ipk : ")
		for x in range(panjang(m)):
			print(m[x].ipk,m[x].nim,m[x].nama)
		print("")
	else:
		print("Index tidak terdaftar\n")

def Searching1(listm,nim_find):
	idx=-1
	for i in range(panjang(listm)):
		if listm[i].nim==nim_find:
			idx=i
			break
	if idx<0:
		return None
	else:
		return listm[idx]

def Searching2(listm,nim):
	idx=-1
	for i in range(panjang(listm)):
		if listm[i].nim == nim:
			idx=i
			break
	return idx
