while True:
    n = float(input('Digite um número positivo: '))
    e = float(input('Digite um expoente positivo para esse número: '))
    if n > 0 and e > 0:
        print(f'A exponencianção de {n:.2f} por {e:.2f} é igual a {n ** e:.2f}')
        break
    else: 
        print('Número inválido, tente novamente')
        print('-' *30)