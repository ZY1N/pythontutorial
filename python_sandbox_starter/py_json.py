# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary

import json


#sample json

userJson = '{"firstname" : "john", "lastname" : "doe", "age" : 30}'

#parse to dict
user = json.loads(userJson)

print(user)
print(user['firstname'])

car = {'make' : 'ford', 'mode' : "mustang", 'year' : 666}

carJson = json.dumps(car)

print(carJson)