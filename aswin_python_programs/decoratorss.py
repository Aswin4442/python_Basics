# # @ symbol with decorator 

# def make_pretty(func):
#     def inner():
#         print("i got decorated")
#         func()
#     return inner
# @make_pretty
# def ordinary():
#     print("iam ordinary")
# ordinary()

# def frnds(names):
#     def inner():
#         print("aswin")
#         names()
#         return 
    
# def outer():
#     print("akash")
#     return outer
# @frnds
# def brthrs():
#     print("karthik")
# brthrs()


# def multiply(func):
#     def inner(x,y):
#         print("multiply",x,"to",y)
#         if y ==0:
#             print("the answer is 0")
#             return
#         return func(x,y)
#     return inner
# @multiply
# def multiple(x,y):
#     print(x*y)

# multiple(5,10)
# multiple(3,23)
# multiple(2,0)
