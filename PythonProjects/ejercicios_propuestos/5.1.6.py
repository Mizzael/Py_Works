# Crea un programa que pida al usuario 5 números reales y luego muestre el menor de todos ellos (pero sin almacenar todos los valores).
from random import *

less_value = 10000

for valores in range(0, 5):
    num = input('Type a number: ')
    if int(num) <= int(less_value):
        less_value = num

print(f'The less is: {less_value}')
