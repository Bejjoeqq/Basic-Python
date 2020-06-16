from math import *
def panjang(data):
	cnt=0
	if data==None:
		return cnt
	else:
		for i in data:
			cnt+=1
		return cnt

def BacaTabelInt():
	d=[0]*int(input("Panjang Tabel Integer : "))
	if panjang(d)>20:
		d=d[:20]
	return d

def TulisTabelData(data):
	ln=panjang(data)
	if ln<1:
		print('{}')
	else:
		print('{',end="")
		for i in data:
			if 0<ln-1 :
				print(i,",",end="")
			else:
				print(i,end="")
			ln-=1
		print("}")

def CariElm(data,elm):
	found=None
	for e in data:
		if e==elm:
			found=e
			break
	return found

def CariIdx(data,elm):
	found=None
	for i in range(panjang(data)):
		if data[i]==elm:
			found=i
			break
	return found

def getValueMax(data):
	maxim=-9999
	for i in data:
		if maxim<i:
			maxim=i
	return maxim

def getIndexMax(data):
	maxim=-9999; idx=-1
	for i in range(panjang(data)):
		if maxim<data[i]:
			maxim=data[i]
			idx=i
	return idx

def countingSort(data,minim,maxim):
	cnt=[0]*(maxim-minim+1)
	for x in data:
		cnt[x-minim]=cnt[x-minim]+1
	sorted=[0]
	for x,n in enumerate(cnt,minim):
		for i in range(n):
			sorted=sorted+[x]
	return sorted

def counting_sort_mm(data,minim,maxim):
	p=panjang(data)
	size=maxim-minim+1
	count=[0]*size
	for i in range(0,p):
		count[data[i]-minim]=count[data[i]-minim]+1
	for i in range(minim,maxim):
		z=0
		for j in range(0,count[i-minim]-1):
			data[z]=i
			z=z+1
	return data

def selectionSort(data):
	p=panjang(data)
	for i in range(0,p):
		m=i
		for j in range(i,p):
			if data[j]<data[m]:
				m=j
		t=data[i]
		data[i]=data[m]
		data[m]=t
	return data


def insertionSort(data):
	p=panjang(data)
	for i in range(1,p):
		tmp=data[i]
		j=i
		while (j>0 and tmp<data[j-1]):
			data[j]=data[j-1]
			j=j-1
		data[j]=tmp
	return data

