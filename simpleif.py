#1. Write an if statement that prints "Equal" if a is equal to b.
a=int(input("enter number : "))
b=int(input("enter number : "))
if a==b:
 print("equal")

#2. How would you write an if statement to check if a number num is greater than 100.
num=int(input("enter number : "))
if num>100:
    print("num is greater than 100")

#3.	Wr ite an if statement that prints "Too low" if a variable temperature is less than 32.
num=int(input("enter temperature: "))
if num<32:
    print("Too Low")

#4.	How can you use an if statement to check if a variable x is positive and print "Positive" if true?
num=int(input("enter number: "))
if num>0:
    print("Positive")
#5.	Write an if statement to print "Negative" if a variable value is less than 0.
num=int(input("enter number: "))
if num<0:
    print("Negative")

#6.	How would you write an if statement to check if a variable count is exactly 0?
count=int(input("enter number: "))
if count==0:
    print("zero")

#7. Write an if statement that prints "Match" if a string variable text is equal to "hello".
text=input("enter number: ")
if text=='hello':
    print("Match")

#8.	How can you use an if statement to check if a string username is not empty?
username=input("enter number: ")
if username !='':
    print("not empty")

#9.	Write an if statement to check if a boolean variable flag is True.
flag=int(input("enter number: "))
if flag ==True :
    print("true")

#10.	How can you use an if statement to check if an item x is in a list my_list?
mylist=["hello",3,4,5]
x=eval(input("enter x item : "))
if x==mylist:
    print("x is in my list")

#11.	Write an if statement to check if the key 'name' exists in a dictionary info.
info={
    "name":["rani","ram"]
}
if "name" in info:
    print("key,name")

#12.How can you use an if statement to check if a function is_valid(value) returns True?
value=input("enter any function: ")
if value in dir(str):
    print("valid")


#13.Write an if statement to print "None found" if a variable data is None.
data=None
if data is None:
    print("None found")

#14. How would you write an if statement to execute  code only if a variable active is True?
active = True
if active:
    print("The code is executing because active is True.")

#15. Write an if statement that prints "Inactive" if a variable enabled is False.

enabled = False
if not enabled:
    print("Inactive")

#16.How can you write an if statement to check if two strings str1 and str2 are not equal?

str1=input("enter number: ")
str2=input("enter number: ")

if str1 !=str2:
    print("not equal")

#17.Write an if statement to check if a number num is even and print "Even".
num=int(input("enter any number : "))
if num%2==0:
 print("even")

#18.How would you write an if statement to check if a number num is odd?
num=int(input("enter any number : "))
if num%2!=0:
 print("odd")

#19.Write an if statement to check if a character ch is uppercase.
ch=input("enter character: ")
if 'A' <= ch <= 'Z':
    print("Character is uppercase")

#20.Write an if statement to check if a character ch is lowercase.
ch=input("enter character: ")
if 'a' <= ch <= 'z':
    print("Character is lowercase")

ch=input("enter character: ")
if ch.islower():
    print("Character is lowercase")

#21.Write an if statement to check if a list my_list contains more than 5 elements.
my_list = eval(input("enter any data :"))
if len(my_list) > 5:
    print("The list contains more than 5 elements.")


#22.How would you write an if statement to check if a variable score is equal to 100?
scope=int(input("enter any no : "))
if scope==100:
    print("scope is equal to 100")

# 23.Write an if statement to print "List is empty" if a list items is empty.
li=eval(input("enter list items : "))
if type(li) is '':
    print("List is empty")

#24.How can you use an if statement to check if the condition x > 10 is true?
x=int(input("enter any no : "))
if x>10:
    print("true")

#25.Write an if statement to check if a variable obj is of type int.
obj=eval(input("enter list items : "))
if type(obj) in [int]:
    print("type int ")

#26.How would you write an if statement to check if a number age is between 18 and 30?
age=int(input("enter any no : "))
if age>18 and age<30:
    print("age is between 18 and 30")

# 27.Write an if statement to check if the value at index 2 in a list values is greater than 50.
ind=eval(input("enter list items : "))
if ind[2]>50 :
    print("list values is greater than 50 ")

# 28.How can you use an if statement to check if a string text has a length of exactly 5.
text=input("enter list items : ")
if  len(text) == 5:
    print("string text has a length of exactly 5")

# 29.Write an if statement to check if a number num is a multiple of 5.
num=int(input("enter list items : "))
if num%5==0:
    print("num is a multiple of 5")


   

