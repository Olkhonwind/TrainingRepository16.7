class Cat:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age


cats = [{'name': 'Барон', 'gender': 'мальчик', 'age': 2}, {'name': 'Сэм', 'gender': 'мальчик', 'age': 2 }]
# print(cats)
for cat in cats:
    all_cat = Cat(name=cat.get("name"), gender=cat.get("gender"), age=cat.get("age"))

    #print(f'\nимя: {all_cat.name}\tпол: {all_cat.gender}\tвозраст: {all_cat.age}')