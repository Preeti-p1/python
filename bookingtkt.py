# movies=["chhava","marco","creature"]
# prices=[250,300,350]
# seats=[35,45,40]
# timming=["10:30 am ", "1:30 pm","2:00 pm"]

# movies_name=input("enter any movie name :")

# if movies_name.strip() in movies:
#  if movies_name.strip()==movies[0]:
#     print(f"Movie name {movies[0]} price {prices[0] } Available seats {seats[0]} Timming {timming[0]}")
#     booking=int(input("how many tickets "))
#     total=prices[0]*booking
#     print("total price",total)
#     gst=total*18/100
#     print("Pay Total Amount",total+gst)
#     print("Thank you ! payment successful😊")
#  elif movies_name.strip()==movies[1]:
#     print(f"Movie Name {movies[1]} Price {prices[1] } Available seats {seats[1]} Timming {timming[1]}")
#     booking=int(input("how many tickets "))
#     total=prices[1]*booking
#     print("total price",total)
#     gst=total*18/100
#     print("Pay Total Amount",total+gst)
#     print("Thank you ! payment successful😊")
#  elif movies_name.strip()==movies[2]:
#     print(f"Movie name {movies[2]} Price {prices[2] } Available seats {seats[2]} Timming {timming[2]}")
#     booking=int(input("how many tickets "))
#     total=prices[2]*booking
#     print("total price",total)
#     gst=total*18/100
#     print("Pay Total Amount",total+gst)
#     print("Thank you ! payment successful😊")
# else:
#    print("This movie is not avaliable")

# 10.wap if the length of string is even then reverse else convert into upper case (take user input)
val=input("enter a str :  ")
if len(val)%2==0:
 print("rev" ,val[::-1])
else:
   print("A"<=val<="Z")