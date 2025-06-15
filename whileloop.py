# 1.wap to print the names only if the length of the names is even
l=["vaidegi","ashwini","patil","srinidhi","susmitha","rahul","priyanka","usha"]
even=[]
i=0
while i<len(l):
    if len(l[i])%2==0:
     even.append(l[i])
    i+=1
print(even)

# 2.wap to print the elements which in tuple,print only the if it is collection data types
values=(10,2.5,[10,20],"hero",True,(3,4,5),{2,7},{90:"super"})
i=0
while i<len(values):
   if isinstance(values[i], (list, tuple, set, dict)):
        print(values[i])
   i+=1


while i<len(values):
    if type(values[i]) in [list ,tuple,set ,dict,str]:
        print(values[i])
    i+=1


# 3.wap to print the name which is starting with vowel in the given list
names=["agra","bangalore","mumbai","pune","indore","isha","eshwar","surat"]
vname=[]
i=0
p=0
while i<len(names):
    if names[i][p] in "AEIOUaeiou":
        vname.append(names[i])
    i+=1
print(vname)

# 4..wap to print sum of numbers in the list
l=[2,4,6,7,8,9]
sum=0
i=0
while i<len(l):
   sum +=l[i]
   i+=1
print(sum) 

# 5.wap to extract only vowels and digits from the given string
s="hellopython123"
i=0
r=''
while i<len(s):
   if s[i] in 'aeiouAEIOU123456789':
    r+=s[i]
   i+=1
print(r)

# 6. wap to print the sum of n natural numbers.
n=int(input("enter any no :"))
sum=0
i=1
while i<=n:
    sum += i
    i += 1
print(sum)

# 7. wap to find the factorial of a number.
n=int(input("enter any no : "))
fact=1
i=1
while i<=n:
    fact*=i
    i+=1
print(n , "factorial is :", fact)

# 8. wap to extract all the lower case characters present in a string taken as input from the user.
user=input("enter any string ")
low_case=''
i=0
while i<len(user):
    if "a"<=user[i]<="z":
        low_case+=user[i]
    i+=1
print(low_case)

# 9. wap tp extract all the special characters present in a string taken as input but the user.
user=input("enter any string ")
low_case=''
i=0
while i<len(user):
    if user[i] in '!@#$%^&*()_ ':
        low_case+=user[i]
    i+=1
print(low_case)

# 10. wap to extract all the digits present in the string taken as input from the user.
user=input("enter any string ")
low_case=''
i=0
while i<len(user):
    if user[i] in '1234567890 ':
        low_case+=user[i]
    i+=1
print(low_case)

#  11. wap to extract all the values at even index given in a list only if they are float values.
li=[12,"hello",34,"ki",22.3,43,90.5,5.5,8.9]
i=0
float_value=[]
while i<len(li):
    if type(li[i]) == float:
        float_value.append(li[i])
    i+=2
print(float_value)




# 12.wap to find the sum of all the integer numbers present inside given tuple.
values = (10, 2.5, [10, 20], "hero", True, (3, 4, 5), {2, 7}, {90: "super"}, 15, 8)
sum = 0
i = 0 
while i < len(values):
    if isinstance(values[i], int) and not isinstance(values[i], bool): 
        sum += values[i]  
    i += 1 
print("Sum of all integer numbers in the tuple:", sum)



# 13.wap to print a number which are divisible by 5 from a list
l=[63,20,67,55,85,31]
i=0
while i<len(l):
    if l[i]%5==0:
        print(l[i])
    i+=1


# 14.wap to print both upper and lower case characters.
gh="fjsdhfhgsdfhDTXRFgjD"
i=0
up=""
lo=""
while i<len(gh):
    if "A"<=gh[i]<="Z":
        up+=gh[i]
    elif "a"<=gh[i]<="z":
        lo+=gh[i]
    i+=1
print(up)
print(lo)




