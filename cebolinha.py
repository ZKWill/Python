frase = 'Isso é errado, raios e trovões'
frase_dividida = frase.split(' ')
frase_trocada = []

for p in frase_dividida:
    if 'r' not in p[0] and 'r' not in p[-1]:
        frase_trocada.append(p.replace('r', 'l'))
    else:
        frase_trocada.append(p)

print(frase_trocada)