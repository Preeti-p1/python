# class Company:
#     Cname="xyz"
#     Ceo="Aryan"
#     Cloc="uganda"
#     Cphno=420
#     def __init__(self,name,eid,sal):
#         self.name=name
#         self.eid=eid
#         self.sal=sal
#     def display(self):
#         print(f"name:{self.name}")
#         print(f"eid:{self.eid}")
#         print(f"sal:{self.sal}")
#         # monkey patching
#     monkey=display
#     @classmethod
#     def display(cls):
#         print(f"Cname:{cls.Cname}")
#         print(f"Ceo:{cls.Ceo}")
#         print(f"Cloc:{cls.Cloc}")
#         print(f"Cphno:{cls.Cphno}")
# e1=Company("nishant",250,10000)
# e1.display()
# e1.monkey()

# operator overloading
# class arthmetic:
#     def __init__(self,num):
#         self.num=num
#     def __add__(self,second):
#         return self.num+second.num
#     def __sub__(self,second):
#         return self.num-second.num
#     def __mul__(self,second):
#         return self.num*second.num
#     def __truediv__(self,second):
#         return self.num/second.num
#     def __floordiv__(self,second):
#         return self.num//second.num
#     def __mod__(self,second):
#         return self.num%second.num
#     def __mod__(self,second):
#         return self.num**second.num
# s1=arthmetic(3)
# s2=arthmetic(4)
# s3=arthmetic(5)
# s4=arthmetic(9)
# print(s1+s2)
# print(s1-s2)
# print(s3*s4)
# print(s3/s4)
# print(s1//s2)
# print(s1%s2)
# print(s1**s2)

