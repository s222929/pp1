person = {
    "name": "Marek",
    "surname": "Banach",
    "age": 25,
    "hobby": ["swimming","excursions"],
    "married": True,
    "phone":{"landline":"123444321","mobile":"777888999"}
   }

print(person)
print(person['name'])
print(person['hobby'])

person['surname'] = "Nowak"
print(person['surname'])

person['married'] = False
print(person['married'])

person['gender'] = "Male"
print(person['gender'])
person["hobby"].append("bicycle")
print(person["hobby"])


