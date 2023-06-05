#Program to write and read employee recrods in the binary file

import pickle

bfile = open('empfile.dat','wb')
recno = 1

print('Enter records of Employees')
print()

#taking data as input from user
while True:
    print('Record no : ',recno)
    
    eno = int(input('Enter Employee number : '))
    ename = input('Enter Employee name : ')
    ebasic = int(input('Enter the basic salary : '))
    allow = int(input('Enter the allowances : '))
    totsal = ebasic + allow
    print('Total Salary = ',totsal)
    
    edata = [eno,ename,ebasic,allow,totsal]
    pickle.dump(edata,bfile)
    
    ans = input('Do you wish to enter more records? (y/n)')
    recno += 1
    if ans.lower() == 'n':
        print('Record Entry OVER')
        print()
        break
    
#retriving the size of the file
print('The size of the binary file is : ',bfile.tell())

bfile.close()

#reading the employee records from binary file using load mode
bfile = open('empfile.dat','rb')
readrec = 1
while(readrec < recno):
    print('Record number : ',readrec)
    data = pickle.load(bfile)
    print(data)
    readrec += 1
    
bfile.close()