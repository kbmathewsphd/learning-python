#reating an array from user req
arr=[]
arrq = int(input("what is the number of elements? "))
for i in range (arrq):
    val = int(input("enter no "))
    arr.append (val)
print (arr)

flag=False
#traversing through array
num = int(input("number to be checked "))
for i in range (len(arr)):
    if (num == arr [i]):
         flag=True

if flag:
   print("find")
else:
    print("nop")
