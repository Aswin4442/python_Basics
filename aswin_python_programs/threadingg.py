# import threading


# def print_cube(num):
#     print("Cube: {}" .format(num * num * num))


# def print_sum(num1,num2):
#     print("Square: {}" .format(num1 + num2))


# if __name__ =="__main__":
#     t1 = threading.Thread(target=print_sum, args=(10,12))
#     t2 = threading.Thread(target=print_cube, args=(10,))

#     t1.start()
#     t2.start()

#     t1.join()
#     t2.join()

#     print("Done!")



import threading

# num = int(input("Enter a number: "))
def print_cube(num):
    print("cube: {}" .format(num*num*num))
   
def print_square(num):
    print("square: {}" .format(num*num))

def print_sum(num1,num2):
    print("sum: {}" .format(num1+num2))

if __name__ =="__main__":
    user= int(input("Enter a number: "))
    user2=int(input("Enter a number: "))

    t1=threading.Thread(target=print_cube, args=(user,))
    t2=threading.Thread(target=print_square, args=(user,))
    t3=threading.Thread(target=print_sum, args=(user,user2,))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print("finished !")

    