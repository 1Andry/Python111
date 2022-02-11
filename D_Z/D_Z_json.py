import json
from random import choice

persons = {}


def get_person():
    numb = ""
    name = ""
    tel = ""
    liters = ["a", "b", "c", "d", "i", "f", "g", ]
    num = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    while len(numb) != 11:
        numb += choice(num)
    while len(name) != 7:
        name += choice(liters)
    while len(tel) != 9:
        tel += choice(num)
    persons[numb] = {"name": name, "tel": tel}
    return persons


for i in range(5):
    get_person()
print(persons)
with open("persons.json", "a") as f:
    json.dump(persons, f, indent=2)

get_person()
