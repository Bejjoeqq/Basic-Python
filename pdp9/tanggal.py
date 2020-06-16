import math
T={
	"hari":29,
	"bulan":2,
	"tahun":2016
}
def ResetTanggal():
	global T
	T["hari"]=1
	T["bulan"]=1
	T["tahun"]=1901
def IsValidT(h,b,t):
	if b==1 or b==3 or b==5 or b==7 or b==8 or b==10 or b==12:
		return h>=1 and h<=31
	elif b==4 or b==6 or b==9 or b==11:
		return h>=1 and h<=30
	elif b==2:
		if IsKabisat(t)==False:
			return h>=1 and h<=28
		else:
			return h>=1 and h<=29
	else:
		return False
def IsKabisat(Y):
	if Y % 100 == 0:
		return Y % 400 == 0
	return Y % 4 == 0
def MakeTanggal(h,b,t):
	global T
	if IsValidT(h,b,t)==True:
		T["hari"]=h
		T["bulan"]=b
		T["tahun"]=t
	else:
		ResetTanggal()
def getHari(T):
	return T["hari"]
def getBulan(T):
	return T["bulan"]
def getTahun(T):
	return T["tahun"]
def BacaTanggal():
	h,b,t = map(int, input("Baca Tanggal : ").split('/'))
	MakeTanggal(h,b,t)
	return h,b,t
def TulisTanggal(T):
	return "{}/{}/{}".format(T["hari"],T["bulan"],T["tahun"])
def HariKe(T):
	b=1
	total=0
	while True:
		if b==1 or b==3 or b==5 or b==7 or b==8 or b==10 or b==12:
			total+=31
		elif b==4 or b==6 or b==9 or b==11:
			total+=30
		elif b==2:
			if IsKabisat(T["tahun"])==False:
				total+=28
			else:
				total+=29
		else:
			return False
		if b==T["bulan"]:
			return total
		b+=1
def DayofMonth(b,y):
	if b==1 or b==3 or b==5 or b==7 or b==8 or b==10 or b==12:
		return 31
	elif b==4 or b==6 or b==9 or b==11:
		return 30
	elif b==2:
		if IsKabisat(y)==False:
			return 28
		else:
			return 29
	else:
		return False
def NextDay(T):
	b=T["bulan"]
	if b==1 or b==3 or b==5 or b==7 or b==8 or b==10 or b==12:
		if b!=12:
			if T["hari"]==31:
				T["bulan"]+=1
				T["hari"]=1
			else:
				T["hari"]+=1
		else:
			if T["hari"]==31:
				T["tahun"]+=1
				T["bulan"]=1
				T["hari"]=1
			else:
				T["hari"]+=1

	elif b==4 or b==6 or b==9 or b==11:
		if T["hari"]==30:
			T["bulan"]+=1
			T["hari"]=1
		else:
			T["hari"]+=1
	elif b==2:
		if IsKabisat(T["tahun"])==False:
			if T["hari"]==28:
				T["bulan"]+=1
				T["hari"]=1
			else:
				T["hari"]+=1
		else:
			if T["hari"]==29:
				T["bulan"]+=1
				T["hari"]=1
			else:
				T["hari"]+=1
def PrevDay(T):
	b=T["bulan"]
	if T["hari"]-1!=0:
		T["hari"]-=1
	else:
		if T["bulan"]-1!=0:
			T["bulan"]-=1
			if b==1 or b==3 or b==5 or b==7 or b==8 or b==10 or b==12:
				T["hari"]=31
			elif b==4 or b==6 or b==9 or b==11:
				T["hari"]=30
			elif b==2:
				if IsKabisat(T["tahun"])==False:
					T["hari"]=28
				else:
					T["hari"]=29
		else:
			T["tahun"]-=1
			T["bulan"]=12
			T["hari"]=31

def NextNDay(T,N):
	b=T["bulan"]
	h=T["hari"]+N
	if b==1 or b==3 or b==5 or b==7 or b==8 or b==10 or b==12:
		if b!=12:
			if h>=31:
				T["hari"]=h-31
				T["bulan"]+=1
			else:
				T["hari"]+=N
		else:
			if h>=31:
				T["tahun"]+=1
				T["bulan"]=1
				T["hari"]=h-31
			else:
				T["hari"]+=N
	elif b==4 or b==6 or b==9 or b==11:
		if h>=30:
			T["bulan"]+=1
			T["hari"]=h-30
		else:
			T["hari"]+=N
	elif b==2:
		if IsKabisat(T["tahun"])==False:
			if h>=28:
				T["bulan"]+=1
				T["hari"]=h-28
			else:
				T["hari"]+=N
		else:
			if T["hari"]>=29:
				T["bulan"]+=1
				T["hari"]=h-29
			else:
				T["hari"]+=N
def PrevNDay(T,N):
	h=T["hari"]
	if h-N<=0:
		h-=N
		T["bulan"]-=1
		b=T["bulan"]
		if b==1 or b==3 or b==5 or b==7 or b==8 or b==10 or b==12:
			T["hari"]=31+h
		elif b==4 or b==6 or b==9 or b==11:
			T["hari"]=30+h
		elif b==2:
			if IsKabisat(T["tahun"])==False:
				T["hari"]=28+h
			else:
				T["hari"]=29+h
	else:
		T["hari"]=h-N
def IsEqD(T1,T2):
	return T1==T2
def IsBefore(T1,T2):
	if T1["tahun"]<=T2["tahun"]:
		if T1["bulan"]<=T2["bulan"] and T1["tahun"]<=T2["tahun"]:
			if T1["hari"]<T2["hari"] and T1["bulan"]<=T2["bulan"] and T1["tahun"]<=T2["tahun"]:
				return True
			else:
				return False
		else:
			return False

	else:
		return False

def IsAfter(T1,T2):
	if T1["tahun"]>=T2["tahun"]:
		if T1["bulan"]>=T2["bulan"] and T1["tahun"]>=T2["tahun"]:
			if T1["hari"]>T2["hari"] and T1["bulan"]>=T2["bulan"] and T1["tahun"]>=T2["tahun"]:
				return True
			else:
				return False
		else:
			return False

	else:
		return False
