# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

#create dict

person = {
    'first_name': 'John',
    'last_name' : 'doe',
    'age' : 30
}

#use constrcutor
#person2 = dict(firstname = 'sara', lastname = 'whocares')

#get value
print(person['first_name'])
print(person.get('last_name'))

#add key/val
person['phone'] = '324234234234'


#get dict keys
print(person.keys())

#get dict keys
print(person.items())

#copy dict
person2 = person.copy()
person2['city'] = 'boston'

print(person2)

#remove item
del(person['age'])
person.pop('phone')

#clear
person.clear()

#get length
print(len(person2))
print(person)

#list of dict
people = [
    {'name' : 'martba', 'age' : 30},
    {'name' : 'ken', 'age' : 333}
]

print(people[1]['name'])