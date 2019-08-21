# Python has functions for creating, reading, updating, and deleting files.


#open file
myFile = open('myfile.txt', 'w')

#getinfo 
print('name: ', myFile.name)
print('name: ', myFile.closed)
print('name: ', myFile.mode)

#write to file
myFile.write('i love python')
myFile.write('and javascript')
myFile.close()

#append to file
myFile = open('myfile.txt', 'a')
myFile.write('and i also like php')
myFile.close()

#read from file
myFile = open('myfile.txt', 'r')
text = myFile.read(100)
print(text)
myFile.close()