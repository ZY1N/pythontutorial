# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Brad'
age = 37

#concatonate
#print("Hello, my name is" + name + "and i am " + str(age))

# String Formatting

#arguments by position
#print("my name is {name} and i am {age}".format(name=name, age=age))

#fstring 3.6+
#print(f"helli, my name is{name} and i am {age}")

# String Methods

s = "hello world"

#capitalize string
print(s.capitalize())

s.upper()
.lower
.swapcase
.len
.replace()
count
.startswith
.endswith
.split #split it into a list
.find
.isalnum
.isalpha
.isnumeric
.