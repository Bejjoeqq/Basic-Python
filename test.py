arrayA = [11,3,2,5,1,6,9] #Array A dengan isi default
print(arrayA[-3])
for x in arrayA:
    print( x ,end=" ")

print("")
for x in range(len(arrayA)): #for x in range(panjang_array)
    print(x,end=" ")

print("")
variabelKosong = None #cara membuat variabel kosong yang bisa diisi dengan string,int,float,boolean (tidak bisa melakukan increament/decreament)
# for x in range(1,10):
#     variabelKosong += str(x) --> error karena variabel bertipe None
arrayB = list() #cara membuat array kosong, cara lain : arrayB=[]

print(arrayB) #print arrayB
for x in range(1,10):
    arrayB.append(x) #menambahkan index array dari paling ujung kanan
print(arrayB) #print hasil arrayB

arrayC =[x for x in arrayB] #bentuk lain membuat array
for x in range(len(arrayC),0,-1): #print index terbalik cara 1
    print(x,end=" ")

print("")
for x in arrayC: #print index terbalik cara 2
    print(arrayC[-x],end=" ")
print("")
 #note ArrayC[-1] = dimulai dari index paling kanan, Ex:
 #ArrayC=[ 5, 6, 2, 4]
 #        -4,-3,-2,-1  ->> indexnya
