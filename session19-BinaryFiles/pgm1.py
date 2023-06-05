#using binary files
import pickle

#Write a string into a binary file
binary_file_handle = open('file1.dat','wb')

pickle.dump("I love computers",binary_file_handle)
binary_file_handle.close()

#Read the data from binary file and display it on terminal
binary_file_handle = open('file1.dat','rb')
data = pickle.load(binary_file_handle)
print(data)
binary_file_handle.close()