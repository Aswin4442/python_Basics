# exception handling using try and except

# try:
#     numerator=10
#     denominator=0
#     result=numerator/denominator
#     print(result)
# except:
#     print("error : denominator can be 0.")

# example 2 

# try:
#     even_numbrs=[2,4,6,8]
#     print(even_numbrs[5])
# except IndexError:
#     print("Index out of bound.")

# using string exmaples

# try:
#     text="hello world !"
#     char=text[20]
# except IndexError as a:
#     print(f"IndexError occurred : {a}")


# using else block 

# try:
#     fruits=["apple","banana","orange"]
#     print(fruits[2])
# except IndexError:
#     print("index out of bound")
# else:
#     print("succesfully accessed the list elements")


# using finally block 

# try:
#     x=10
#     y=0
#     result=x/y
# except ZeroDivisionError:
#     print("cannot divide by zero")
# finally:
#     print("this block always run")


