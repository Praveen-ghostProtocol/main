#WAP to store a list of tuples (names,marks) in a binary file.
#Read the binary file and display the data

import pickle
list_of_names = [('Arjun',100),('Bhaskar',90),('Chethan',80),('Don',70)]

binary_file_handle = open('names_binary.dat','wb')
pickle.dump(list_of_names,binary_file_handle)
binary_file_handle.close()

binary_file_handle = open('names_binary.dat','rb')
data = pickle.load(binary_file_handle)
for name,marks in data:
    print(name+"    "+str(marks))
binary_file_handle.close()