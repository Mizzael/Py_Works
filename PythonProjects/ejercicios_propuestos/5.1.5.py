# Crea un programa que pida al usuario 5 números reales, los guarde en una lista y luego muestre el menor de todos ellos (Pista: para calcular el mínimo de una serie de datos deberemos partir de un valor inicial e irlo comparando con todos los de la lista; si el valor actual es menor que el mínimo, pasará a ser nuestro nuevo mínimo; en cuanto a ese "valor inicial", una forma "peligrosa" de obtenerlo es partir de uno claramente incorrecto, como "1000000" (que es mayor que todos los de la lista), y una forma más fiable es tomar como valor inicial el primer dato de la lista y después compararlo con los restantes).
from random import *

list_num_rand = []

for index_list_num_rand in range(0, 5):
    rnum = randrange(10)
    list_num_rand.append(rnum)

print(f'Your list is: {list_num_rand}')
print(f'The less value in your list is: {min(list_num_rand)}')
