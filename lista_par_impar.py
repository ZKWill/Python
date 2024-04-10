lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
pares = []
impares = []

for c in lista:
    if c % 2 == 0:
        pares.append(c)
    if c % 2 == 1:
        impares.append(c)

print(f'A lista dos pares é {pares}')
print(f'A lista dos ímpares é {impares}')