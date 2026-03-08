#vowel count
#get data from user
count = 0
vow = input("enter the string ")
for i in vow:
    if i in "aeiou":
        count+=1 #count = count +1
print (count)