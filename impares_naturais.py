from time import sleep
n = int(input('Insira um número: '))
print(f'Esses são os números ímpares até o número {n}')
print('Calculando...')
for c in range(0, n):
    if c % 2 == 1:
        print(f'{c} ', end='')
        sleep(1)