# write in zipfile

# import zipfile
# with zipfile.ZipFile("zip_text.zip","w")as f:
#     f.write("new_file1.csv")
#     f.write("new_file2.csv")

# read in zipfile

# import zipfile
# with zipfile.ZipFile("zip_text.zip","r")as f:
#     f.extractall("zippedfile")
#     list1=f.namelist()
#     print(list1)


# my example

# import zipfile
# with zipfile.ZipFile("zip_text.zip","w")as f:
#     f.write("food.csv")
#     f.write("text.csv")

# with zipfile.ZipFile("zip_text.zip","r")as f:
#     f.extractall("zippedfile2")
#     list2=f.namelist()
#     print(list2)