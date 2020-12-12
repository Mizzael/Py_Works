def suma(valor_1, valor_2):
    return int(valor_1)+int(valor_2)


def resta(valor_1, valor_2):
    return int(valor_1)-int(valor_2)


def multi(valor_1, valor_2):
    return int(valor_1)*int(valor_2)


def div(valor_1, valor_2):
    return int(valor_1)/int(valor_2)


print('Opciones\n1.Suma\n2.Resta\n3.Multiplicación\n4.División\n5.Cerrar')
while True:
    opc = input('¿Qué deseas hacer? ')
    if opc in ('1', '2', '3', '4'):
        var1 = input('Ingresa el primer valor: ')
        var2 = input('Ingresa el segundo valor: ')
        if opc == '1':
            print('La suma de: '+str(var1)+' + ' +
                  str(var2)+' es: '+str(suma(var1, var2)))
        elif opc == '2':
            print('La resta de: '+str(var1)+' - ' +
                  str(var2)+' es: '+str(resta(var1, var2)))
        elif opc == '3':
            print('La resta de: '+str(var1)+' * ' +
                  str(var2)+' es: '+str(multi(var1, var2)))
        elif opc == '4':
            print('La resta de: '+str(var1)+' / ' +
                  str(var2)+' es: '+str(div(var1, var2)))
            break
    else:
        print("Opcion incorrecta, intentalo de nuevo")
