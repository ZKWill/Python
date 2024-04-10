lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

print('Lista de 0 a 9: ')
for c in lista:
    if lista[c] <= 9:
        print(lista[c], end=' ')
print('\n')

print('Lista de 8 a 13: ')
for c in lista:
    if lista[c] >= 8 and lista[c] <= 13:
        print(lista[c], end=' ')
print('\n')

print('Números Pares: ')
for c in lista:
    if lista[c] % 2 == 0:
        print(lista[c], end=' ')
print('\n')

print('Números Ímpares: ')
for c in lista:
    if lista[c] % 2 == 1:
        print(lista[c], end=' ')
print('\n')

print('Múltiplos de 2: ')
for c in lista:
    if lista[c] % 2 == 0:
        print(lista[c], end=' ')
print('\n')

print('Múltiplos de 3: ')
for c in lista:
    if lista[c] % 3 == 0:
        print(lista[c], end=' ')
print('\n')

print('Múltiplos de 4: ')
for c in lista:
    if lista[c] % 4 == 0:
        print(lista[c], end=' ')
print('\n')

lista.sort(reverse = True)
print(f'A lista invertida fica {lista}')