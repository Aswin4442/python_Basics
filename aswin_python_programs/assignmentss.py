# create a list, access indexing and convert to tuple and find type

# mylist=["apple","bmw",30,True,24]
# print(mylist[2])
# print(mylist[-4])
# x=tuple(mylist)
# print(x)
# print(type(mylist))
# print(type(x))


# create dict and access keys and values 

# mycar={
#     "brand":"bmw",
#     "model":"m5",
#     "hp":"768hp"
# }
# print(mycar)
# x=mycar.keys()
# y=mycar.values()
# print(x,y)
# for x in mycar:
#     print(mycar[x])


# find a factorial of a number


# Python program to find the factorial of a number provided by the user.

# change the value for a different result
# num = 7

# # To take input from the user
# num = int(input("Enter a number: "))

# factorial = 1

# # check if the number is negative, positive or zero
# if num < 0:
#    print("Sorry, factorial does not exist for negative numbers")
# elif num == 0:
#    print("The factorial of 0 is 1")
# else:
#    for i in range(1,num + 1):
#        factorial = factorial*i
#    print("The factorial of",num,"is",factorial)



# factorial=1
# num=int(input("Enter a number"))
# if num<0:
#     print("factorial not exist for negative number")
# elif num ==0:
#     print("the factorial of 0 is 1")
# else:
#     for x in range(1,num + 1):
#         factorial=factorial*x

#     print("the factorial of",num,"is",factorial)


# create a tuple with single element

# mycar=("bmw")
# print(mycar)

# create tuple with 6 element , print the corresponding index 

# tuple=("apple","bmw",11,56,True)
# new=list(tuple)
# print(new)
# index=enumerate(new)
# print(list(index))
   

# def find_sum(*numbers):
#     result=0
#     for x in numbers:
#         result= result + x
#     print("answer =",result)
# find_sum(23,30,67)



#  num=int(input("enter a digit"))
# def find_factorial(*numbers):
#         factorial=1
#         for x in range(1,num+1):
#               factorial *=x
#         print("factorial =",factorial)
# find_factorial()


# # 7- 11-2024

# 1

# class details:
#     def __init__(self):
#         self.name=input("enter a word__")
# x=details()
# print(x.name.upper())

#2


# class details:
#     def __init__(self,name,age,gender,course,place):
#         self.name=name
#         self.age=age
#         self.gender=gender
#         self.course=course
#         self.place=place
# p1=details("karthik",20,"male","python","alpy")
# print("name   :",p1.name)
# print("age    :",p1.age)
# print("gender :",p1.gender)
# print("course :",p1.course)
# print("place  :",p1.place)    

# 3

# class circle:
#     @staticmethod
#     def radius(r):
#         if r==0:
#             pass 
#         else:
#             return 3.14*r*r
# print("area : ",circle.radius(5))

# import math
# n=int(input("enter a number :"))
# print(math.pi)













