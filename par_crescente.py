while True:
    n = int(input('Digite um número par: '))
    if n % 2 == 0:
        print(f'\033[1mPerfeito! Iniciando a contagem de 1 até {n}\033[m')
        break
    else:
        print('Esse número não é par, tente novamente')
for c in range(0, n):
    print(f'{c + 1}', end=' ')