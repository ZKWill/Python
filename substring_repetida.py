frase = 'frase de teste'
frase_dividida = frase.split(' ')
lista_palavras = []
palavras_maior = []

print(frase_dividida)

for p in frase_dividida:
    for l in p:
        if (p.count(l) <= 1):
            lista_palavras.append(p)

for p in frase_dividida:
    if (len(p) == lista_palavras.count(p)):
        palavras_maior.append(p)

print(max(palavras_maior))