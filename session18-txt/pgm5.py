# ASSIGNMENT:
# 1. Program to read the contents of source file, convert the first letter and last letter of 
# every word into upper case and store it in a target file. 
# Accept the source file and target file from the user.


source = input('Enter source file name : ')
target = input('Enter target file name : ')

f_source = open(source,'r')
f_target = open(target,'w')

list = f_source.readlines()
for line in list:
    result =  ''
    for word in line.title().split():
        result += word[:-1] + word[-1].upper() + ' '
    f_target.write(result[:-1]+'\n')
    
f_target = open(target,'r')
print(f_target.read())