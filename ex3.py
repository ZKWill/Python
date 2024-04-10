nome_pontuador = ''
mais_pontos = 0

for r in range (1, 4):
    nome = str(input(f'Diga o nome do jogador da {r}º rodada: '))
    pontos = int(input('Insira a pontuação do jogador: '))

    if pontos > mais_pontos:
        nome_pontuador = nome
        mais_pontos = pontos

arquivo = open('ex3.txt', 'w')
arquivo.write(f'O nome do maior pontuador é {nome_pontuador}\nEle marcou um total de {mais_pontos} pontos')
print(f'O nome do maior pontuador é {nome_pontuador}\nEle marcou um total de {mais_pontos} pontos')