# 5.1.2. Crea un programa que pida al usuario 10 números enteros, los guarde en un array y luego le pregunte de forma repetitiva qué número quiere buscar. Le responderá si dicho número estaba o no entre los datos que se habían introducido inicialmente. Dejará de repetirse cuando se introduzca el número 0.

array = []

for index in range(0, 10):
    array.append(int(input(f'Valor {index+1}: ')))

while True:
    num = int(input('¿Qué número buscas? '))
    if num in array:
        print('Si se encuentra')
    elif num not in array:
        print('No se encuentra')
    if num == 0:
        break
