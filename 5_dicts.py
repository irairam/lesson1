# Создайте словарь:
# {"city": "Москва", "temperature": "20"}
# Выведите на экран значение ключа city
# Уменьшите значение "temperature" на 5
# Выведите на экран весь словарь

from pprint import pprint
testdict = {
    'city': 'Moscow',
    'temperature': 20
    }

print(testdict['city'])
testdict['temperature'] = testdict['temperature'] - 5
print(testdict)

# Проверьте, есть ли в словаре ключ country
# Выведите значение по-умолчанию "Россия" для ключа country
# Добавьте в словарь элемент date со значением "27.05.2019"
# Выведите на экран длину словаря
print(testdict.get('Country','Russia'))
testdict['date']='27.05.2019'
print(len(testdict))
pprint(testdict,width=20)