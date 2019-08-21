# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

#create calss
class User:
    #consturcter, function that runs when you instantiate a object from a class
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
    
    def greeting(self):
        return f'my name is {self.name} and i am {self.age}'
    
    def has_birthday(self):
        self.age += 1

# extend class
class Customer(User):
    #consturcter, function that runs when you instantiate a object from a class
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
    
    def set_balance(self, balance):
        self.balance = balance
    
    #def greeting(self):
       # return f'my name is {self.name} and i am {self.age}, and my balance is {self.balance}'

# init user object

brad = User('brad traversey', 'brad@gmail.com', 37)

#init customer obj
janet = Customer('janet johnson', "janet@gmail.com", 666)

janet.set_balance(500)
print(janet.greeting())

#print(brad.name, brad.age)
brad.has_birthday()
print(brad.greeting())