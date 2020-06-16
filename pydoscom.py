# for x in range(1,10):#pyramid atas
#     print("* "*x)
# for y in range(10,0,-1):#pyramid bawah
#     print("* "*y)

# for x in range(10):
#     for y in range(x,-1,-1):
#         print("{:4d}".format(2**y),end=" ")
#     print("")

# for x in range(8):#1
#     for y in range(8):#4
#         if x==y or x+7==y:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print("")
z=10
temp=0
for x in range(1,z):
    temp=z//2
    for y in range(0,x):
        pass
        print(" "*temp+"*")
