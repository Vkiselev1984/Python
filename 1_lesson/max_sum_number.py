
import unittest

"""
Найдите сумму цифр трехзначного числа n.
Результат сохраните в перменную res.
"""

n = 123
import warnings
warnings.filterwarnings('ignore')

n1 = n // 100 # Нахождение первой цифры числа
n2 = (n % 100) // 10 # Нахождение второй цифры числа
n3 = n % 10 # Нахождение третьей цифры числа
res = n1 + n2 + n3

print(res)

"""
Альтернативный вариант

"""
def sum_of_digits(n):
    if not isinstance(n, int) or not 100 <= n <= 999:
        raise ValueError("Число должно быть трехзначным в диапазоне от 100 до 999")
    return sum(int(digit) for digit in str(n))

result = sum_of_digits(n)

print(result)

class TestSumOfDigits(unittest.TestCase):
    def test_sum_of_digits(self):
        self.assertEqual(sum_of_digits(123), 6)
        self.assertEqual(sum_of_digits(999), 27)
        
    if __name__ == '__main__':
        unittest.main()
        