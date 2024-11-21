# # static method

# class calculator:
#     @staticmethod
#     def addnumbers(x,y):
#         return x+y
# print("sum :",calculator.addnumbers(100,50))

# # find factorial

# class numbers:
#     @staticmethod
#     def factorial(n):
#         if n==0:
#             return 1
#         else:
#             return n*numbers.factorial(n-1)
# print(numbers.factorial(5))


# # class method

# class person:
#     age = 25
#     def printage(cls):
#         print("the age is :",cls.age)
# person.printage=classmethod(person.printage)
# person.printage()

# from datetime import date
# class person:
#     def __init__(self,name,year):
#         self.name=name
#         self.year=year
#         @classmethod
#         def birth_year(cls,name,year):
#             return cls(name,date.today(),year-birth_year)
#     def display(self):
#             print("name is :",self.name, "    " "birth year is :",self.year)
# prsn1=person("karthik",2003)
# prsn1.display()

