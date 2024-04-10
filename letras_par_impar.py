nome = str(input('Diga o seu nome: '))
letras_nome = len(nome)

if letras_nome % 2 == 0:
    print(f'O nome possui uma quantidade par de letras! ({letras_nome})')
else:
    print(f'O nome possui uma quantidade ímpar de letras! ({letras_nome})')