# Задание 1
# Пройдите по списку ['Вася', 'Маша', 'Петя', 'Валера', 'Саша','Даша']
# Пока не встретите имя Валера. Когда найдете - напишите "Валера нашелся".
# Используйте list.pop()

names = ['Вася', 'Маша', 'Петя', 'Валера', 'Саша','Даша']
while names[0] != 'Валера':
    names.pop(0)
print('Валера найден')

# Задание 2
# Перепишите предыдущий пример в виде функции find_person(name), 
#которая ищет имя в списке

names = ['Вася', 'Маша', 'Петя', 'Валера', 'Саша','Даша']

def find_person(name):
     #Сказано использовать list.pop - так и быть ) 
     #Но сначала прогоним через if. 
    if name in names:
        while names[0] != name:
            names.pop(0)
        print(f'Вы искали: {name}. {name} найден в списке')
    else:
        print(f'Вы искали: {name}. {name} НЕ найден в списке')

name = find_person(input('Кого ищем? '))

# Задание 3
# Напишите функцию ask_user() чтобы с помощью input спрашивать как дела,
# пока не ответит "Хорошо"

def ask_user():
    while True:
        user_say = input('One more time. Kak dela?: ')
        if user_say == 'Хорошо':
            print('Nice. Bye')
            break
        else: 
            print (f'{user_say} is a wrong answer! Try again')
if __name__ == '__main__':
    ask_user()

# 4 задание
# При помощи функции get_answer() отвечать на вопросы юзера в ask_user(), 
# пока не скажет "Пока!"

import random

answers = ['wow!','i"m so excited!', 'go on!', 'nice weather today']

def ask_user2():
    while True:
        user_say = input('Kak dela?: ')
        if user_say == 'Хорошо':
            print('Продолжайте в том же духе!')
            break
        else:
            print(random.choice(answers))
            get_answer()

def get_answer():
    while True:
        user_will = input('Поговорим?: ')
        if user_will == 'Пока!':
            print('Отлично. Приходите еще!')
            exit() #break именно в этом месте не выводит из цикла почему-то
        else: 
            ask_user2()

if __name__ == '__main__':
    get_answer()
