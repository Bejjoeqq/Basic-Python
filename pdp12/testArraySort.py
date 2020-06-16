from arraySort import *

data1=[2,42,32,12,22,39,15,8,4,20]

def main():
	TulisTabelData(data1)
	print("Cari 22 dalam data : {}".format(CariElm(data1,22)))
	print("Cari idx elemen 22 : {}".format(CariIdx(data1,22)))
	print("Elemen Max data1   : {}".format(getValueMax(data1)))
	print("Index Max data1	   : {}".format(getIndexMax(data1)))
	sorted1=countingSort(data1,0,9999)
	TulisTabelData(sorted1)
	sorted2=selectionSort(data1)
	TulisTabelData(sorted2)
	sorted3=insertionSort(data1)
	TulisTabelData(sorted3)
	sorted4=counting_sort_mm(data1,0,9999)
	TulisTabelData(sorted4)

	print("\nTa da !")
if __name__ == '__main__':
	main()
