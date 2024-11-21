# access modifiers 

# 1. public 

# class Student:
#    def __init__(self, name, age):
#       self.name = name
#       self.age = age
    
#    def display(self):
#       print("Name:", self.name)
#       print("Age:", self.age)

# s = Student("John", 20)
# s.display() 

#  2. private 

# class bankaccount:
#    def __init__(self,account_number,balance):
#       self.__accountnumber=account_number
#       self.balance=balance
#       def __display_balance(self):
#         print("balance :",self.__balance)
# b=bankaccount(1234567890,3000)
# b.__display_balance()

# class BankAccount:
#    def __init__(self, account_number, balance):
#       self.__account_number = account_number
#       self.__balance = balance
    
#    def __display_balance(self):
#       print("Balance:", self.__balance)

# b = BankAccount(1234567890, 5000)
# b.__display_balance() 


# 3. protected

# class person:
#     def __init__(self,name,age):
#         self._name=name
#         self._age=age
    
#     def _dispaly(self):
#         print("name :",self._name)
#         print("age :",self._age)

# class student(person):
#     def __init__(self,name,age,roll_number):
#         super().__init__(name,age)
#         self._roll_number=roll_number
    
#     def dispaly(self):
#         self._dispaly()
#         print("roll number :",self._roll_number)
# s=student("karthi",20,28)
# s.dispaly()


