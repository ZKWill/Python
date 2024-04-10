lista = []
for c in (0, 6):
    num = int(input('Digite um número: '))
    lista.append(num)
lista.sort(reverse=True)
print(f'Foram digitados {len(lista)} números')
if 5 in lista:
    print('O número 5 está na lista')
else:
    print('O número 5 não está na lista')
print(lista)