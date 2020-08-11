https://drive.google.com/file/d/1BfLQd0H04crZz7zUgaXl9oHbUTxfZhbD/view?usp=sharing 

# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

a = int(input('Введите любое трехзначное число: '))
b = a // 100
c = (a // 10)%10
d = a % 10
# print(b)
# print(c)
# print(d)
print(c + d + b)
print(c * b * d)
