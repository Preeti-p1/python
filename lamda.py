# LAMBDA

# 1.wap to find square and cube of given number
# a=lambda i :i**2 if i%2==0 else i**3
# print(a(int(input("enter any no : "))))

# 2.wap to check the given number is palindrome or not
# p=lambda i : 'plaindrome' if i==i[::-1] else 'not'
# print(p(input("enter any string ")))

# 3.wap to convert negative number to positive number
# p=lambda i : i if i>0 else -i 
# print(p(int(input("enter any no "))))

# 4.wap to return the key of a dictionary
# a={"hello":"Sony","How":"are","you":"bye"}
# get_key =lambda i :list(map(lambda item:item[0],i.items())) 
# print(get_key(a))

# 5.wap to check if the number is even or odd
# n=lambda i : "even" if i%2==0 else "odd"
# print(n(int(input("enter any no "))))

# 6.wap which returns first element of a sequence
# first_element = lambda seq: seq[0] if seq else None
# print("First element of list:", first_element([10, 20, 30]))
# print("First element of tuple:", first_element((5, 6, 7)))
# print("First character of string:", first_element("Hello"))
# print("Empty list:", first_element([]))  # Will return None

# 7.wap which returns length of any iterable
# l= lambda i :len(i) 
# print("first element of list : ",l([10, 20, 30]))

# 8.wap which returns the list of squares of numbers in a list
# l=[2,3,4,5,6]
# Lambda with map to get squares
# squares = list(map(lambda x: x ** 2, l))
# print("List of squares:", squares)

# 9.wap to check list elements are palindrome or not
# l=["nayana","kayak","mom","school","bag","dad"]
# k=lambda i :k[i] if  k[i]==k[i[::-1]] else 'not'
# print(l)

#10 wap to print the numbers present in a list with their corresponding indices pair 
# l=[100,200,300,400,500]
# l = [100, 200, 300, 400, 500]
# p=lambda pair: print(f"Index: {pair[0]}, Value: {pair[1]}")
# list(map(p, enumerate(l)))

# class exampple

# b=lambda male,female:"eligible" if female>=18 and male>=21 else "not eligible"
# print(b(int(input("enter female age ")),int(input("enter male age  : "))))

# c=lambda i : i.upper() if 'a'<=i<='z' else i
# print(c(input("enter no ")))




