nomes = []
c = 0

for c in range(5):
    nome = str(input('Digite o seu nome: '))
    nomes.append(nome)

for n in nomes:
    print(f'O nome {n} possui {len(n)} letras')