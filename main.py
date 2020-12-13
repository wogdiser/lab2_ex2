# Lab 2
# Вариант 2.
# Zadanie 2
# С помощью генератора сформируйте словарь в котором ключами являются целые числа, а значениями — суммы цифр ключей

import random

def sum_digits(num):
  result = 0
  for char in str(num):
    result = result + int(char)
  return result

dict = {}

for i in range(6):
  key = random.randint(1, 100)
  dict[key] = sum_digits(key)

print(dict)
