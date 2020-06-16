def LinearSearch(k,A):
    found = False
    count = 0
    for i in A:
        if i == k:
            found = True
            count+=1
    return found,count
def BinarySearch(k,A):
    found = False
    batasbawah = 0
    batasatas = len(A)-1
    while batasbawah<=batasatas and not found:
        mid = (batasatas+batasbawah)//2
        if A[mid] == k:
            found = True
        else:
            if A[mid] > k:
                batasatas = mid-1
            else:
                batasbawah = mid+1
    if found == True:
        if k%4==0 and k%6==0:
            k/=3
            print(k)
    return found
def main():
    A=[1,2,4,7,11,12]
    print(LinearSearch(2,A))
    print(BinarySearch(12,A))
if __name__ == '__main__':
    main()
