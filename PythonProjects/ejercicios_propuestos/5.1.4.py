# 5.1.4. Crea un programa que pida al usuario las componentes de dos vectores de 3 elementos. Después debe mostrar el módulo de cada uno de los vectores, así como su producto escalar.
import math

vector_a = []
vector_b = []
value = 0


def module_vector(vector):
    square_elements = []
    for i in range(len(vector)):
        square_elements.append(pow(int(vector[i]), 2))
    return math.sqrt(sum(square_elements))


angle = input('Inset the angle value: ')
for a in range(0, 3):
    value = input('Insert the value in Vector A: ')
    vector_a.append(value)
    if a >= 2:
        for b in range(0, 3):
            value = input('Insert the value in Vector B ')
            vector_b.append(value)

print(f'The module of Vector A is: {str(module_vector(vector_a))}')
print(f'The module of Vector A is: {str(module_vector(vector_b))}')

scalar_product = (int(module_vector(vector_a)) *
                  int(module_vector(vector_b)))*math.cos(int(angle))

print(f'The scalar product is: {scalar_product}')
