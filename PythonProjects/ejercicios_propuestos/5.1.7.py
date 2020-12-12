# Crea un programa que pida al usuario un bloque de 3x3 números enteros y luego muestre la media de las tres filas.
import random as rdn

matriz = []

for rows in range(0, 3):
    matriz.append([])
    for colums in range(0, 3):
        matriz[rows].append(rdn.randrange(10))

print(matriz)
