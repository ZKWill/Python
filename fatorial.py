import math

def fatorial(numero):
    resultado = math.factorial(numero)
    return resultado

numero = int(input('Digite um número para resolver o fatorial: '))
print(f'O fatorial do número é {fatorial(numero)}')