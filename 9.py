# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

a = int(input('Первое число: '))
b = int(input('Воторе число: '))
c = int(input('Третье число: '))

if a < b < c or c < b < a:
    print(b)
elif a < b < c or c < b < a:
    print(a)
else:
    print(c)
    
