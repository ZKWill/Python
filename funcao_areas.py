import math

def area(figura, *args):
    if figura == 1:
        lado = args[0]
        return lado ** 2
    
    if figura == 2:
        base, altura = args
        return (base * altura) / 2
    
    if figura == 3:
        raio = args[0]
        return math.pi * (raio * raio)
 
print('1 - Quadrado\n'
    '2 - Triangulo\n'
    '3 - Circulo\n')
figura = int(input('Esolha uma das opções acima para calcular a area: '))

if figura == 1:
    lado = float(input('Insira o valor dos lados do quadrado: '))
    print(f'A área do quadrado é {area(figura, lado)}')
elif figura == 2:
    altura = float(input('Insira a altura do triângulo: '))
    base = float(input('Insira o tamanho da base do triângulo: '))
    print(f'A área do triângulo é {area(figura, base, altura)}')
elif figura == 3:
    raio = float(input('Insira o raio do círculo: '))
    print(f'A área do círculo é {area(figura, raio)}')
else:
    print('Opção inválida, tente novamente!')
