abast = float(input('Insira quantos reais serão usados no abastecimento: '))
vlrl = float(input('Insira o valor do litro do combustível: '))
litabas = abast / vlrl
print('Com R${}, você irá abastecer {}l de combustível'.format(abast, litabas))
