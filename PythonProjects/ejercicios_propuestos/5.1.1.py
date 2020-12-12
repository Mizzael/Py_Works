# 5.1.1. Crea un programa que pida al usuario 10 números enteros y luego muestre los que eran pares, todos ellos en la misma línea separados por un espacio en blanco.

numeros = {}

for i in range(0, 10):
    valor = int(input(f'Valor {i+1}: '))
    numeros[i] = valor

for i in range(0, len(numeros)):
    if numeros[i] % 2 == 0:
        print(numeros[i], end=" ")
