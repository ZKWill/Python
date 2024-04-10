arquivo = open('ex1.txt', 'a')

nome = str(input('Diga o seu nome: '))
escrita = arquivo.write(nome)

arquivo_lido = open('ex1.txt', 'r')
seu_nome = arquivo_lido.readlines()

print(f'Seja bem vindo! {seu_nome[0]}')