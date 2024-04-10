contnove = 0
pares = 0
dez_vinte = 0
media = 0
valores = (int(input('Digite um número: ')),
           int(input('Digite um número: ')),
           int(input('Digite um número: ')),
           int(input('Digite um número: ')))

for c in valores:
    if c == 9:
        contnove += 1

if 3 in valores:
    for n, t in enumerate(valores):
        if t == 3:
            print(f'O valor três apareceu pela primeira vez na posição {n}º')
if 3 not in valores:
    print('O valor 3 não está na tupla')

for c in valores:
    if c % 2 == 0:
        pares += 1

for c in valores:
    if c >= 10 and c <= 20:
        dez_vinte += 1

for c in valores:
    media += c

print(f'O 9 apareceu {contnove} vez(es)')
print(f'Existem {pares} números pares na tupla')
print(f'Existem {dez_vinte} números que estão entre 10 e 20')
print(f'A média dos valores é de {media / 4:.0f}')