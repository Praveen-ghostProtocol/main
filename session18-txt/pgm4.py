#program to read from a source file and write it into a target file
# accept the source file name and target file name from the user.


source = input('Enter source file name : ')
target = input('Enter target file name : ')

f_source = open(source,'r')
f_target = open(target,'w')

f_target.write(f_source.read())
f_source.close()
f_target.close()

f_target = open(target,'r')
print(f_target.read())

# #4. Program to read from a source file and write it into a target file. 
# # Accept the source file name and target file name from user.


# #Step 1 - Prompt and accept the source file name
# source_filename = input("Enter the source file name : ")

# #Step 2 - Prompt and accept the target file name
# target_filename = input("Enter the target file name : ")

# #Step 3 - Open the source file in read mode
# source_fp = open(source_filename, 'r')

# #Step 4 - Read from the source file pointer and store it in a string
# file_contents_str = source_fp.read()

# #Step 5 - Open the target file in write mode
# target_fp = open(target_filename, 'w')

# #Step 6 - Write the string data into the target file
# target_fp.write(file_contents_str)

# #Step 7 - Close the source file
# source_fp.close()

# #Step 8 - Close the target file
# target_fp.close()
