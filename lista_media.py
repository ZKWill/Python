soma = 0
notas = [7.9, 6.5, 8.0, 9.0]

for c in notas:
    soma += c

print(f'A média das notas é igual a {soma / 4}')
notas.sort()
print(f'As notas são {notas}')