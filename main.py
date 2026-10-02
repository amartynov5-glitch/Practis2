a = int(input('Введите номер месяца:'))
if a > 12:
    print('Неверный номер месяца')
if 3 <= a <= 5:
    print('Весна')
if 6 <= a <= 8:
    print('Лето')
if 9<=a<=11:
    print('Осень')
elif 1<=a<=2 or a ==12:
    print('Зима')
