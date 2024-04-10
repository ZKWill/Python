from time import sleep
s = 0
n = int(input('Insira um número: '))
print(f'Calculando a soma dos números naturais até {n}...')
sleep(1)
print('.')
sleep(1)
print('.')
sleep(1)
print('.')
sleep(1)
print('Quase lá...')
sleep(1)
print('\033[1mTudo pronto!\033[m')
for c in range(0, n + 1):
    s += c
print(f'A soma de todos dos números naturais até {n} é {s}')