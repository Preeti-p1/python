# exception handling :
# the process of handling the exception which may occur at the runtime of any program.

# Exception is an unexcepted event and error that may occur durring the execution process.

# The core components of Python's exception handling are:

# 1.try block: This block contains the code that might raise an exception.

# 2. except block: If an exception occurs within the try block, the program execution jumps to the corresponding except block. This block handles the specific exception or exceptions caught. Multiple except blocks can be used to handle different types of exceptions. 

# 3else block (optional): This block executes if no exception occurs within the try block.

# 4.finally block (optional): This block always executes, regardless of whether an exception occurred or not. It is typically used for cleanup operations, such as closing files or releasing resources.

# 5.raise statement: This statement is used to explicitly trigger an exception. This is useful for signaling errors in custom functions or when a specific condition warrants an exception.

# we can perform exception handling  by three ways :- specific exception handling ,generic exception handling ,default exception handling


# specific exception handling
# try:
#     numerator =int(input("eneter any no : "))
#     denominator =int(input("eneter any no : "))
#     result = numerator / denominator  # This will raise a ZeroDivisionError
#     print(f"Result: {result}")
# except ZeroDivisionError:
#     print("Error: Cannot divide by zero.")
# except TypeError:
#     print("Error: Invalid data type for operation.")
# else:
#     print("Division successful.")
# finally:
#     print("Execution complete.")




# generic exception handling


# try:
#     a =int(input("eneter any no : "))
#     b =int(input("eneter any no : "))
#     r=a/b
# except Exception:
#     print("invalid !")
# else:
#     print("successfull !")
# finally:
#     print("you code is executed ")


# try:
#     i=1
#     while i>0:
#         print(i)
#         i+=1
# except Exception:
#     print("invalid")

# default exception handling
# try:
#     i=1
#     while i>0:
#         print(i)
#         i+=1
# except :
#     print("invalid")

# try:
#     x = int(input("enter: "))  # This will cause ValueError
    
#     #inverse
#     inv = 1 / x
    
# except ValueError:
#     print("Not Valid!")
    
# except ZeroDivisionError:
#     print("Zero has no inverse!")



try:
    file = open("geeks.txt", "r")
    content = file.read()
    print(content)
finally:
    file.close()