#program to read from a txt file and display

fp = open('fruits2b.txt','r')

print('-----read-----')
data = fp.read()
print(data)

print('-----readline-----')
fp.seek(0)
line = fp.readline()
print(line.strip())

line = fp.readline()
print(line.strip())

line = fp.readline()
print(line.strip())

line = fp.readline()
print(line.strip())

line = fp.readline()
print(line.strip())
print('----------')

print('Before seeking: The value of file pointer: ',fp.tell())
fp.seek(0)
print('After seeking: The value of file pointer: ',fp.tell())

print('--------readlines-------')
list = fp.readlines()
for line in list:
    print(line.strip())
print('----------')