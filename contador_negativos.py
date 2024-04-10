somneg = 0
for c in range(0, 5):
    n1 = int(input('Digite um número: '))
    if n1 < 0:
        somneg += 1
print(f'Foram digitados {somneg} números negativos')
