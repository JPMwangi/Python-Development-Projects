# 1. Read files you can use this method. open and close kwargs.

# file = open("Day 24 file system/my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# you may use the with statement. 
# with open('Day 24 file system\my_file.txt') as file:
#     contents = file.read()
#     print(contents)
    
# 2. Write to the file.
# with open('Day 24 file system\my_file.txt', mode="a") as file:
#     # 'w is write. replaces contents in the file
#     file.write('1. johnpeter is a Kenyan Citizen.')
#     # to append contents in the file use 'a'
#     file.write('\n2. johnpeter is a Kenyan Citizen.')

# 3. create a new file in the directory
with open("../../new_file.txt") as file:
    c = file.read()
    print(c)
# absolute dir is /Users/User/Desktop/new_file.txt