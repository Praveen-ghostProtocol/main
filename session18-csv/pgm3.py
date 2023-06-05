#read a csv file

import csv 

fp = open('students2.csv','r')
reader = csv.reader(fp)

print('-'*100)
for row in reader:
    for col in row:
        print(col,'|',end=' ')
    print()
        
print('-'*100)