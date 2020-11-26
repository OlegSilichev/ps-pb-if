# Работа с оператором if

# Объявление переменных
cities = ['Москва', 'Париж', 'Лондон']

users = [{'name': 'Иван', 'age': 35},
         {'name': 'Мария', 'age': 22},
         {'name': 'Соня', 'age': 20}]

tourists = [{'user': users[0], 'city': cities[2]},
            {'user': users[1], 'city': cities[0]},
            {'user': users[2], 'city': cities[1]}]

city = input('Введите город: ') # Запрос на ввод города

# Проверяем есть ли введеный город в списке cities и определяем кто там был    
if (len(city) > 0) and ((city.lower() in cities[0].lower()) or (city.lower()
   in cities[1].lower()) or (city.lower() in cities[2].lower())):
    if tourists[0]['city'].lower() == city.lower():
        print (f"Турист {users[0]['name']} возраст {users[0]['age']}. Посетил город {city} ")
    elif tourists[1]['city'].lower() == city.lower():
        print (f"Турист {users[1]['name']} возраст {users[1]['age']}. Посетил город {city} ")
    elif tourists[2]['city'].lower() == city.lower():
        print (f"Турист {users[2]['name']} возраст {users[2]['age']}. Посетил город {city} ")
else:
    print("В данном городе никто из туристов не бывал")
