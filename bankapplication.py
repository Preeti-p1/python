username=input("Enter name : ")
password=input("Enter password :")

while  password!="python":
 password=input("enter:")
print("sucessfully login 😊 !")
print("Enter 0 = Check Current Balance")
print("Enter 1 = Deposite Balance")
print("Enter 2 = withdraw Balance")
user=int(input("Enter any no :"))
current=10000
if user==0:
       print(f"you current balance is {current}")      
elif user==1:
        amount=int(input("Enter Deposite Amount : "))
        deposite=current+amount
        print(f"Now you current  amount is {deposite}")
elif user==2:
        withdraw=int(input("enter withdraw amount : "))
        if withdraw>current:
            print("Amount is not sufficent!")
        else:
            print(f"withdraw is succesful😊😊")  
else: 
     print("invalid number 😒!")