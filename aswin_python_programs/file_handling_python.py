# STEP 1 = creating a file in python

# file1=open("demofile.txt","x")

# STEP 2 = writing a file 

# file1=open("demofile.txt","w")
# file1.write("HELLO GOOD MORNING")
# file1.close()

# STEP 3 = reading the file

# file1=open("demofile.txt","r")
# print(file1.read())

# STEP 4 = append another content in file

# File1=open("demofile.txt","a")
# lines=[", HAVE A NICE DAY ! \n","iam karthi \n"]
# File1.writelines(lines)
# File1.close()

# file1=open("demofile.txt","r")
# print(file1.read())


# READ METHODS 

# pick specific characters 

# file1=open("demofile.txt","r")
# print(file1.read(5))

# read line 

# file1=open("demofile.txt","r")
# print(file1.readline())

# read lines 

# file1=open("demofile.txt","r")
# print(file1.readlines())


# WRITING METHODS

# write lines

# file1=open("demofile.txt","w")
# lines=["this line is 1\n","this line is 2\n","this line is 3\n"]
# file1.writelines(lines)
# file1.close()

# delete the file 

# import os
# os.remove("demofile.txt")



# 2 my example

# myfile=open("my file.txt","x")
# myfile=open("my file.txt","w")
# myfile.write("HELLO !")
# myfile=open("my file.txt","a")
# myfile.write(" , IAM KARTHIK\n")
# myfile.close()
# myfile=open("my file.txt","a")
# lines=["BEST FRIENDS :\n","ASWIN\n","AKASH\n"]
# myfile.writelines(lines)
# line2=["IAM A PYTHON FULL STACK DEVELOPER\n"]
# myfile.writelines(line2)
# myfile.close()

# with open("my file.txt", "r") as file1:
#     read_content = file1.read()
#     print(read_content)

