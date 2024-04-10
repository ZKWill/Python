dados = {}
itens = int(input('Digite a quantidade de itens que deseja adicionar ao dicionário: '))

for i in range(itens):
    chave = input('Digite a chave do dicionário: ')
    valor = input('Digite o valor do dicionário: ')

    dados[chave] = valor

print(dados)