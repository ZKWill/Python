altura = float(input('Insira a sua altura: '))
sexo = str(input('Qual o seu sexo? [M/F]')).upper().strip()
if sexo == 'M':
    pesoideal = (72.7 * altura) - 58
    print('Como homem, o seu peso ideal é {:.2f}'.format(pesoideal))
elif sexo == 'F':
    pesoideal = (62.1 * altura) - 44.7
    print('Como mulher, o seu peso ideal é {:.2f}'.format(pesoideal))
else:
    print('Sexo inválido')