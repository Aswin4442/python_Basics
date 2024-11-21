# thisset={"apple","banana","cherry"}
# print(thisset)
# print(type(thisset))

# dupli not allowed 

# x={"apple", "banana", "cherry", True, 1, 2}
# print(x)

# length of a set

# set={"bmw","benz","audi"}
# print(len(set)) 

# set items

# set1 = {"a", "b", "c"}
# set2 = {1, 5, 7, 9, 3}
# set3 = {True, False, False} 
# set4=(set1,set2,set3)
# print(set4)

# thisset={"abc",0,34,False,True,"cars"}
# print(thisset)

# access set items

# set={"apple", "banana", "cherry"}
# for x in set:
#     print(x)

# x={"bmw","benz","audi"}
# print("bmw" in x)

#  add set items

# set = {"apple", "banana", "cherry"}
# set.add("orange")
# print(set) 

# update func

# set = {"apple", "banana", "cherry"}
# set2 = {"pineapple", "mango", "papaya"}
# set.update(set2)
# print(set) 

# remove set items

# set={"apple", "banana", "cherry"}
# set.remove("banana")
# print(set)

# discard func

# set = {"apple", "banana", "cherry"}
# set.discard("banana")
# print(set) 

# pop func

# a = {"apple", "banana", "cherry"}
# x = a.pop()
# print(x)
# print(a) 

# clear func

# thisset = {"apple", "banana", "cherry"}
# thisset.clear()
# print(thisset) 

# del func

# set = {"apple", "banana", "cherry"}
# del set
# print(set) 

# loop sets

# thisset = {"apple", "banana", "cherry"}

# for x in thisset:
#   print(x) 


# join sets 


# union func 

# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = set1.union(set2)
# print(set3) 

# union or | 

# x={"apple","orange","kiwi"}
# y={"bmw","benz","audi"}
# myset=x | y
# print(myset)

# join multiple set 

# a={"a","b","c","d"}
# b={1,2,3,4,5}
# c={"akash","karthi"}
# d={"bmw","benz"}
# myset=a.union(b,c,d)
# print(myset)

# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = {"John", "Elena"}
# set4 = {"apple", "bananas", "cherry"}

# myset = set1 | set2 | set3 |set4
# print(myset) 

# join a set and tuple 
# x={1,2,3,4}
# y=("a","b","c")
# z=x.union(y)
# print(z)

# update func 

# set1 = {"a", "b" , "c"}
# set2 = {1, 2, 3}
# set1.update(set2)
# print(set1) 


# intersection 

# x={"bmw","benz","audi"}
# y={"bike","caes","bmw"}
# z=x.intersection(y)
# print(z)

# intersection or & 

# set1={1,2,3}
# set2={"a","b",1,"c"}
# myset=set1 & set2
# print(myset)

# intersection update 

# x={"bmw","benz","audi"}
# y={"bike","caes","bmw"}
# y.intersection_update(x)
# print(y)

# set1 = {"apple", 1,  "banana", 0, "cherry"}
# set2 = {False, "google", 1, "apple", 2, True}
# set3 = set1.intersection(set2)
# print(set3)

# diffrence in set

# x= {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# myset =x.difference(y)
# print(myset) 

# difference or - 

# set1={"bmw","benz","audi"}
# set2={"bike",2,"bmw"}
# set3=set1 - set2
# print(set3)

# symmetric difference

# x= {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# z = x.symmetric_difference(y)
# print(z)

# symmetric or ^

# set1={"bmw","supra","GTR"}
# set2={"benz","bmw","chiron"}
# set3=set1 ^ set2
# print(set3)

