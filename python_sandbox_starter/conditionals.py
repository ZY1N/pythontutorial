# If/ Else conditions are used to decide to do something based on something being true or false

x = 3
y = 10

# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values

if x > y:
    print(f'{x} is greater than {y}')

#if/else
#if x > y:
#    print(f'{x} is greater than {y}')
#else:
#    print(f'{y} is greater than {x}')


#elif
if x > y:
    print(f'{x} is greater than {y}')
elif x == y:
    print(f'{y} is equal {x}')
else:
    print(f'{y} is greater than {x}')

#nested if


# Logical operators (and, or, not) - Used to combine conditional statements

#if x > 2 and x <= 10:
 #   print(f"{x} is greater than 2 and less than 10")

#or
#if x > 2 or x <= 10:
 #   print(f"{x} is greater than 2 and less than 10")

#not
#if not x == y:
 #   print(f"{x} is greater than 2 and less than 10")




# Membership Operators (not, not in) - Membership operators are used to test if a sequence is presented in an object

numbers = [1,2,3,4,5]
#in
if x in numbers:
    print(x in numbers)

#not in 

if x not in numbers:
    print(x in numbers)
    
 # Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

#is
if x is y:
    print(x is y)

#is not

if x is not y:
    print(x is y)