while True:
    n = int(input('Digite um número ímpar: '))
    if n % 2 == 1:
        print(f'\033[1mPerfeito! Iniciando a contagem regressiva de 1 até {n}\033[m')
        break
    else:
        print('Esse número não é ímpar, tente novamente')
for c in range(n, 0, -1):
    print(f'{c}', end=' ')