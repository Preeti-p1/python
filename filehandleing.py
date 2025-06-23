# FILE HANDLING :-
#File handling refers to the process of performing operations on a file such as creating, opening, reading, writing and closing it, through a programming interface. It involves managing the data flow between the program and the file system on the storage device, ensuring that data is handled safely and efficiently.



# Open the file and read its contents
# with open('geeks.txt', 'r') as file:
file = open("geeks.txt", "r")
content = file.read()
print(content)
file.close()

print("/"*50)
# read a file in binary mode
file = open("geeks.txt", "rb")
content = file.read()
print(content)
file.close()

# write in a file with write mode
file = open("geeks.txt", "w")
file.write("Hello, World!")
file.write("we are write a write ode fun with w")
file.close()

print("#"*50)
file=open("geeks.txt","r")
con=file.read()
print(con)
file.close()


# Python code to illustrate append() mode
file = open('geeks.txt', 'a')
file.write("This will add hhhh this line")
file.close()

print("#"*50)
file=open("geeks.txt","r")
con=file.read()
print(con)
file.close()


# with open("geeks.txt", "r") as file:
#     content = file.read()
#     print(content)