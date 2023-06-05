#WAP to store a list of names in a binary file.
#Read the binary file and display the data

import pickle
list_of_names = ['Arjun','Bhaskar','Chethan','Don']

binary_file_handle = open('names_binary.dat','wb')
pickle.dump(list_of_names,binary_file_handle)
binary_file_handle.close()

binary_file_handle = open('names_binary.dat','rb')
data = pickle.load(binary_file_handle)
for name in data:
    print(name)
binary_file_handle.close()