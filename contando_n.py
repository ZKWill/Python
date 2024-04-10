from time import sleep
n = int(input('Insira um número: '))
print('Contando...')
for c in range(0, n):
    print(c, end=' ')
    sleep(1)
