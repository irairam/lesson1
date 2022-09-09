# import string
# allowed = set(string.digits + '.')

# def check(price):
#     set(price) <= allowed


#Форматируем, как заказано в задании:
def format_price(price):
    if  set(price).issubset(set('1234567890.')) != True:
        raise ValueError('Можно только числа и точки')
    print(f'Цена: {int(float(price))} руб.')

# Вводим данные:
price = format_price(input('Enter price: '))
