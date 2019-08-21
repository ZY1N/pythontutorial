# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
#create tuple
fruits = ('apples', 'oranges', 'grapes')
#fruits2= tupe((("""""")))

#must have trailing comma or else interpreted as a string
fruits2 = ('Apples',)

#get value
print(fruits[1])

#cant change value
#fruits[0] = 'pears'

#delete tuples
del fruits2

print(len(fruits))

# A Set is a collection which is unordered and unindexed. No duplicate members.

#create set
fruits_set = {'apples', 'oranges', 'mangos'}
#check if in set
print('apples' in fruits_set)

#add to set
fruits_set.add('grape')

#remove from set
#fruits_set.remove('grape')

#add duplicate
fruits_set.add('apples')

#clear set
#fruits_set.clear()

#delete
#del fruits_set

print(fruits_set)