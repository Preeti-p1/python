

# def extract(l):
#     l=[1,2,3,4] 
#     i=0
#     while i<len(l):
#         if i%2==0:
#             print(l[i])
#         i+=1
# extract(eval(input("enter ")))
    


# 1 without argument and return
# def extuple():
#     t=("hello",3,5,"hy")
#     i=0    
#     while i<len(t):
#           if type(t[i])==str:
#             print(t[i])
#           i+=1   
# extuple()

# 2  with argument and without return
# def extuple(t):    
#     i=0    
#     while i<len(t):
#           if type(t[i])==str:
#             print(t[i])
#           i+=1   
# extuple(eval(input("enter tuple : ")))



# 3 without argument and with return

# def extuple(): 
#     t=("hello",3,5,"hy")
#     st=""   
#     i=0    
#     while i<len(t):
#           if type(t[i])==str:
#            st+=t[i]
#           i+=1 
#     return st
# print(extuple())


# output={"hi":[2,"ih"],"hello":[5,"olleh"],}
# def com():
#     l=["hi","hello","how","are","you"]
#     out={}
#     i=0   
#     for i in l:
#         re=i[::-1]
#         count=0
#         for j in i:
#             count+=1
#         out[i]=[count,re]
#     print(out)
# com()

# Do these questions using all 4 types of user defined functions.
# Q1. write a function to remove all the duplicate values present inside the given list.

# def dublicate_val():
#     a=[10,30,10,'hiee','hiee',10]
#     i=0
#     st=set()
#     while i<len(a):
#         st.add(a[i])
#         i+=1
#     return st
# print(dublicate_val())
 

# def dublicate_val():
#     a=[10,30,10,'hiee','hiee',10]
#     i=0
#     st=set()
#     while i<len(a):
#         st.add(a[i])
#         i+=1
#     print(st)
# dublicate_val()

# 12.write a function to print the below output

# def func(s):
#     print(s[1::2])
# func("TRACXN")
 
# def func(s, start):
#     print(s[start::2])

# func("TRACXN", 1)

# Q3. First 10 Natural numbers
# def natural_num():
#     for i in range(1,11):
#         print(i,end=",")
# natural_num()


# 14.A function take variable number of positional arguments
#    as input. how to check if the arguments are more than 5.
# def fun_var(l):
#     # l=[1,2,3,4]
#     if len(l)<5:
#         print(l)
#     else:
#         print("lenth is more then 5")
# fun_var(eval(input("enter no : ")))

# def fun_var(l):
#     # l=[1,2,3,4]
#     if len(l)<5:
#       return l
#     else:
#         print("lenth is more then 5")
# print(fun_var(eval(input("enter no : "))))