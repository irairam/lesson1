# def discounted(price, discount, max_discount=20):
#     price = abs(price)
#     max_discount = abs(max_discount)
#     if max_discount >= 100:
#         raise ValueError('Ahtung!')
#     if discount >= max_discount:
#         price_with_discount = price
#     else:
#         price_with_discount = price - price * discount / 100
#     return price_with_discount

# # price_with_discount=discounted(100,50)
# # price_with_discount= discounted(int(input('введите price:')),int(input('введите discount:')))
# # print(f'Твоя итоговая цена: {price_with_discount}')

# # product = {'name':'Iphone','color':'white','final_price':price_with_discount}
# product = {'name':'Iphone', 'color':'white', 'price':50, 'discount':110}
# product['with_discount'] = discounted(product['price'], product['discount'], max_discount=200)
# print(product)

# Задание 1
# Создайте функцию get_summ(one, two, delimiter='&'), которая принимает два параметра, приводит их 
# к строке и отдает объединенными через разделитель delimiter
# Вызовите функцию, передав в нее два аргумента "Learn" и "python", 
# положите результат в переменную и выведите ее значение на экран
# Сделайте так, чтобы результирующая строка выводилась заглавными буквами

def get_summ(one, two, delimiter='&'):
    if one == ' ' or two == ' ':
        raise ValueError('Пробел не катит')
    if one == '' or two == '':
        raise ValueError('Пустое значение не катит') 
    name = f'{one}{delimiter}{two}'.upper()
    return name

one = input('Enter one:')
two = input('Enter two:')
print('Держи конкатенацию: ',get_summ(one, two))

# Задание 2
# Создайте в редакторе файл price.py
# Создайте функцию format_price, которая принимает один аргумент price
# Приведите price к целому числу (тип int)
# Верните строку "Цена: ЧИСЛО руб."
# Вызовите функцию, передав на вход 56.24 и положите результат в переменную
# Выведите значение переменной с результатом на экран

#Форматируем, как заказано в задании с валидацией:
def format_price(price):
    if  set(price).issubset(set('1234567890.')) != True:
        raise ValueError('Можно только числа и точки')
    print(f'Цена: {int(float(price))} руб.')

# Вводим данные:
price = format_price(input('Enter price: '))