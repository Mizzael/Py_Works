import random

dado = random.randint(1, 6)
print('Lanza el dado\n')
print('Obtuviste un: '+str(dado))
while True:
    anws = input('\n¿Deseas lanzarlo de nuevo?[Si][No]')
    if anws == 'Si' or anws == 'si' or anws == 's':
        print('Obtuviste un: '+str(dado))
    else:
        break
    dado = random.randint(1, 6)
