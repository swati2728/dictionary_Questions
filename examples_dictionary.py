
# city_population = {
#     "NewYorkCity":8550405,
#     "LosAngeles":3971883, 
#     "Toronto":2731571, 
#     "Chicago":2720546, 
#     "Houston":2296224, 
#     "Montreal":1704694, 
#     "Calgary":1239220, 
#     "Boston":667137, 
#     "Boston":"swati"
# }

# ""Keys Case Sensitive :-""

# # # print(city_population["Boston"])
# # print(city_population)
# print(type(city_population))


# Dict = {'ball' : 'green',
#        'Ball': 'red'}
     
# print(Dict['ball'])
# print(Dict['Ball'])
# print(Dict['bat'])

# student=dict(name= "Ravina",age= 20)
# print(student["name"])


# (dictionary with integer keys:-)

# my_dict = {
# 1: 'apple', 
# 2: 'ball'
# }
# print(my_dict[1])

# dictionary with mixed keys:-

# my_dict = {
#     'name': 'John',
#      1: [2, 4, 3]
#     }
# print(my_dict['name'])
# print(my_dict[1])

# Nested Dictionary:-

# Dic= {
#  1: 'NAVGURUKUL',
#  2: 'IN',  
#  3:{
#      'A' : 'WELCOME',
#      'B' : 'To', 
#      'C' : 'DHARAMSALA'
#      }
# }
# print(Dic)

# Accessing Elements from a Dictionary:-

# person={
#     'name':'jack',
#     'age':20,
#     'gender':'male',
#     4:'organisation'}

# result = person['age'] 
# x = person.get("gender")
# print(person[4])
# print(x)
# print(result)

# person={
#     'name':'jack',
#     'age':20,
#     'gender':'male',
#     4:{
#         'organisation':'navgurukul','place':'dharamsala'
#         }
#     }
# print(person['gender'])

# print(person[4])

# result = person[4]['place']

# print(result)

# dic= {
#     'Name': 'RAM', 
#     'Age': 17,
#     }
    
# dic['ORGANIZATION'] = "NAV GURUKUL"

# dic['place'] = 'dharamsala'

# print(dic)

# ========================================================

# Adding Elements to a Dictionary:-
# 1)
# dic= {
#     'Name': 'RAM', 
#     'Age': 17,
#     }
    
# dic['ORGANIZATION'] = "NAV GURUKUL"

# dic['place'] = 'dharamsala'

# print(dic)


# 2)
# dic= {
#    'Name': 'RAM',
#    'Age': 17,
#     }
# dic['student']={
#        'id':22, 
#        'place':'dharamsala'
#    }
# print(dic)

#Key Exists or not

# car ={
# 	"brand":  "ford",
# 	"model":  "mustang",
# 	"year":  1964
# }
# if "model" in car:
#     print("Yes, 'model' is one of the keys in the car dictionary.")

# else:
#     print("No, 'model' key dictionary mai nahi hai.")


# Updating Dictionary :-

# Example 1:-

# person= {'1': 'RAM', '2': 17,}
# person[3] = 'male'
# print(person)

# Example 2:-

# details={
#     'Name': 'RAM',
#      'Age': 17, 
#      'student': {
#       'id': 22,
#       'place': 'dharamsala'
#       }
#      } 
# details['student']['place']='banglore'
# print(details); 

# Copy of Dictionary :-

# Example 1 :-

# classes ={
# 	"room1":  "6th",
# 	"room2":  "7th",
# 	"room3":  "8th"
# 		}
# mydict=classes.copy()
# print(mydict)
# print(classes)

# Removing Elements from a Dictionary:-
 # pop( ) method ka use karke specified element ko remove kar sakte hain :

# CAR_DETAILS={
#     "brand": "Ford",
#     "model": "jason",
#     "year": 1964
# }
# CAR_DETAILS.pop("model")
# print(CAR_DETAILS)

# The popitem() method removes the last inserted item:

person={
    'name':'jack',
    'id':22,
    'place':'dharamsala',
    'family':'love'
}
person.popitem()
print(person)

# Hum del keyword ka use karke kisi specified element ko delete kar sakte hain :

# person={
#     'name':'jack',
#     'id':22,
#     'place':'dharamsala'
# }
# i=dict(person)
# del person['place']
# print(person)

# Iterate through all keys:-
# to print only key

# states_capitals = {
#   'Gujarat' : 'Gandhinagar',
#   'Maharashtra' : 'Mumbai',
#   'Rajasthan' : 'Jaipur',
#   'Bihar' : 'Patna'
#   }
# for state in states_capitals:
#   	print(state)

# Iterate through all values:-
# Example :-

# states_capitals = {
#     'Gujarat' : 'Gandhinagar',
#     'Maharashtra' : 'Mumbai',
#     'Rajasthan' : 'Jaipur',
#     'Bihar' : 'Patna'
#     }
    
# for state in states_capitals:
#     print(states_capitals[state])

# using values funtion


# details ={
# 	"name":  "Bijender",
# 	"age":  17,
# 	"class":  "10th"
# 	}
# for x in details.values():
# 	print(x)

# dictionary se keys and values ek sath kaise print karte hai.

# movie ={
# 	"name":  "Puli",
# 	"hero":  "Vijay",
# 	"rating":  7.5
# 	}
# for x,y in movie.items():
# 	print(x,y)

# Dictionary length
# meal ={
# 	"monday":  "Chole chawal",
# 	"sunday":  "Fried rice",
# 	"wednesday":  "dosa"
# 	}
# print(len(meal))

# i=0
# count=0
# while i < len(meal):
# 	count=count+1
# 	i=i+1
# print(count)	


