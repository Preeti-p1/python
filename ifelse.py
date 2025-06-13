 #if-else assignment(1)

# 1.wap to check the given number is even or odd (take user input)
num=int(input("enter any number : "))
if num%2==0:
 print("even")
else:
 print("odd")

# 2.wap to check whether the male and female are eligible for wedding (take user input)
male=int(input("male age : "))
female=int(input("femal age : "))
if male>=21 and female>=18:
    print("eligible")
else:
    print("not eligible")

# 3.wap to return upper case if the char is lower,else return same char (by taking user input)
ch=input("enter character: ")
if 'a' <= ch <= 'z' :
    print("Character is upper" ,ch.upper())
else:
    print("already upper")

# 4.wap to return lower case if the upper ,else return same char (by taking user input)
ch=input("enter character: ")
if 'A' <= ch <= 'Z' :
    print("Character is lower" ,ch.lower())
else:
    print("already lower")

# 5.wap to find greater value among the two number
# n1=34
# n2=54
n1=int(input("enter any n1 : "))
n2=int(input("enter any n2 : "))
if n1>n2:
    print("n1",n1)
else:
    print("n2",n2)

# 6.wap to check if the given number is even or not,if it is not even add+1 and make it even (take user input)
num=int(input("enter any number : "))
if num%2==0:
 print("even")
else:
 print("even add ",num+1)

# 7.wap to check whether the first character in the given string is starting with uppercase or Not if it is not Then capitalise it
num=input("enter any number : ")
if num[0].islower():
    print("num",num[0].upper()+num[1:])
print(num.capitalize())

# 8.wap to check if the given number is even ,if it is even reduce it to its Half else make exponent (take user input)
num=int(input("enter any number : "))
if num%2==0:
 print("even",num/2)
else:
 print("even add ",num**num)

# 9.wap to check number should be divisible by 3 and 7 (take user input)
num=int(input("enter any number : "))
if num%3==0 and num%7==0:
    print("divided with 3 and 7")
else:
    print("not divided with ")

# 10.wap if the length of string is even then reverse else convert into upper case (take user input)
val=input("enter a str ")
if len(val)%2==0:
 print("val" ,val[::-1])
else:
   print(val.isupper())

# 11.wap to check a number is +ve/-ve number (take user input)
number=int(input("enter a number :"))
if number>0:
    print("postive")
else:
    print("neg")

# 12.wap to check a data is individual or collection data type or not (take user input)
data =eval(input("enter any data :"))
if type(data) in [int,float,str,complex]:
    print("individual")
else:
    print("collection")

# assignment(1)

# 1.wap to check whether the specified character is present in the given string

s = "Python"
char = input("Enter a character to check: ")

if char in s:
    print(f"The character '{char}' is present in the string.")
else:
    print(f"The character '{char}' is not present in the string.")

# 2.wap to check the length of dictionary and length of dictionary is even or Not if even
# print as it is or else add a item and make it even
D={"a":"apple","b":"ball","c":"cat"}
if len(D)%2==0:
    print("even",D)
else:
   D["d"] = "daubi"
print("odd add",D)

# 3.wap to check the given number is greater than 5,if it is greater convert that number into negative number else print the same number
num=int(input("enter any number"))
if num>5:
   num=-num
   print("num",num)
else:
   print(num)

# 4.wap to check the given number is smaller than 10 ,if it is smaller find the exponent of it
# else print the number as it is
num=int(input("enter any number : "))
if num<10:
    print("num",num*num)
else:
   print(num)

# 5.wap to check the given number is odd, if it is odd divide it by 2 and print reminder and quotient else print it is even (take user input)
num=int(input("enter any number :"))
if num%2!=0: 
    quotient = num // 2  # Integer division
    remainder = num % 2  # Modulus operation
    print(f"odd number {quotient} and {remainder}")
else:
   print("even")

# 6.wap to check the given character is alphabets or Not ,if it is alphabet create a replica of it for 2 time. (take user input)
char = input("Enter a character: ")
if char.isalpha():
    print("Replica:", char * 2)
else:
    print("Not an alphabet")


# 7.WAP to check whether the given number value is divisible by 6 or not,if it is divisible cube that number or    else perform left shift operation by 3 (take user input)
num=int(input("enter any number :"))
if num%6==0 :
   print("cube",num**3)
else:
   print("left shift",num<<3)

# 8.wap to check 1st value is pointing towards same memory address of value else print type of that value
a=[1,2,3,4,5]
if id(a[0])==id(a):
   print("same address",id(a[0]),id(a))
else:
   print(type(a))