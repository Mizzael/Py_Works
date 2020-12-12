text = input('Escribe una palabra: ')

contador = 0

vocales = ['a', 'e', 'i', 'o', 'u']

for index in text:
    if index.lower() in vocales:
        contador = contador + 1

print(f'Tiene: {contador} vocales')


words = ['cat', 'mouse', 'dog']
for w in words[:]:
    if len(w) > 3:
        words.insert(0, w)

print(words[0])
