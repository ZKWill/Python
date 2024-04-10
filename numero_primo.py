import math
def primo(numero):
    if numero <= 1:
        return False
    for n in range(2, math.isqrt(numero) + 1):
        if numero % n == 0:
            return False
    return True

numero = int(input('Digite o número a ser testado se é primo ou não: '))
if primo(numero):
    print(f'O número {numero} é primo')
else:
    print(f'O número {numero} não é primo')