maiornum = 0
menornum = 0
for c in range(0, 10):
    n = int(input('Digite um número: '))
    if c == 0:
        maiornum = n
        menornum = n
    if n > maiornum:
        maiornum = n
    if n < menornum:
        menornum = n
print(f'O maior número é {maiornum} e o menor número é {menornum}')