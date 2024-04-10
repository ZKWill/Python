def conversor(escolha, temperatura):
    if escolha == 1:
        return (temperatura * (9/5)) + 32
    elif escolha == 2: 
        return (temperatura - 32) * (5/9)

print('1 - Converter Celsius para Fahrenheit\n'
      '2 - Converter Fahrenheit para Celsius')
escolha = int(input('Esolha uma das opções acima: '))

if escolha < 3:
    temperatura = int(input('Digite a temperatura a ser convertida: '))
else:
    print('Opção inválida, tente novamente!')

if escolha == 1:
    print(f'A conversão de temperatura de Celsius para Fahrenheit é igual a {conversor(escolha, temperatura)}')
elif escolha == 2:
    print(f'A conversão de temperatura de Fahrenheit para Celsius é igual a {conversor(escolha, temperatura)}')