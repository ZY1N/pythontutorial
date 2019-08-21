# A List is a collection which is ordered and changeable. Allows duplicate members.

#basically like an array

#create an list
numbers = [1,2,4,5]
fruits = ["apples", "oranges", "grapes", "pears"]

#use a constructor
#number2= list((1,2,3,4,5))

#print(numbers, number2)

#get a value
print(fruits[1])

#get length
print(len(fruits))

#append to list
fruits.append('mangos')



#remove from list
fruits.remove("grapes")

#insert into position
fruits.insert(2, "strawberries")

#change value
fruits[0] = 'blueberries'

#remove with pop
fruits.pop(2)

#reverse list
fruits.reverse()

#sort list
fruits.sort()

#reverse sort
fruits.sort(reverse = True)
print(fruits)