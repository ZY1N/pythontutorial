# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people = ['john', 'paul', 'sara', 'susan']

#simple for loop

#for person in people:
    #print(f'current person: {person}')

#break
#for person in people:
 #   if person == 'sara':
  #      break
#    print(f'current person: {person}') 

#contineu 
#for person in people:
 #   if person == 'sara':
  #      continue
   # print(f'current person: {person}') 

#range
#for i in range(len(people)):
 #   print(people[i])

#for i in range(0, 11):
 #   print(f'Number: {i}')


# While loops execute a set of statements as long as a condition is true.

count = 0

while count <= 10:
    print(f'count {count}')
    count+= 1