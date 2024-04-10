lista = [1]
continuar = 'S'
while True:
        num = int(input('Digite um número: '))
        continuar = str(input('Deseja continuar?[S/N]'))
        if num not in lista:
            lista.append(num)
        if continuar == 'N':
            break    
lista.sort()
print(lista)