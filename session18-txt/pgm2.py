#program  to write a list of fruit names in a file in different lines

list_of_fruits = ['Apple\n','Banana\n','Guava\n','Watermelon\n','Jackfruit\n']

fp = open('fruits2b.txt','w')

# for i in range(len(list_of_fruits)):
#     fp.write(list_of_fruits[i])

fp.writelines(list_of_fruits)