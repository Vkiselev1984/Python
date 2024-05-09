"""
Счастливым билетом называют такой билет с шестизначным номером, 
где сумма первых трех цифр равна сумме последних трех.
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
Вам требуется написать программу, которая проверяет счастливость билета 
с номером n и выводит на экран yes или no.
"""
n = 385916  # Пример числа

n1 = n // 100000
n2 = (n % 100000) // 10000
n3 = (n % 10000) // 1000
n4 = (n % 1000) // 100
n5 = (n % 100) // 10
n6 = n % 10
if n1 + n2 + n3 == n4 + n5 + n6:
    print('yes')
else:
    print('no')
    
"""
Альтернативное решение
"""

n_str = str(n)
digits_sum_front = sum(int(digit) for digit in n_str[:3])
digits_sum_back = sum(int(digit) for digit in n_str[3:])

if digits_sum_front == digits_sum_back:
    print('yes')
else:
    print('no')
