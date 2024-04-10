while True:
    n = int(input('Digite um número par: '))
    if n % 2 == 0:
        print(f'\033[1mPerfeito! Iniciando a contagem regressiva de 1 até {n}\033[m')
        break
    else:
        print('Esse número não é par, tente novamente')
for c in range(n, 0, -1):
    print(f'{c}', end=' ')