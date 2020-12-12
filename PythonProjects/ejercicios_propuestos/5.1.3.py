# 5.1.3. Crea una variante del programa 5.2 que no sólo diga si el número estaba o no, sino que informe de cuántas veces se ha encontrado.
array = []

for index in range(0, 10):
    array.append(int(input(f'Valor {index+1}: ')))

while True:
    num = int(input('¿Qué número buscas? '))
    if num in array:
        print('Si se encuentra')
        print('Y se encontro: '+str(array.count(num))+' veces')
    elif num not in array:
        print('No se encuentra')
    if num == 0:
        break
