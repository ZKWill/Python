notas = {'Português' : 8, 'Matemática' : 8.5, 'História' : 9, 'Geografia' : 6, 'Arte' : 7}
media = 0
menor_nota = 100

for i in notas:
    print(i, notas[i])
    media += notas[i]
    if notas[i] < menor_nota:
        chave = i
        menor_nota = notas[i]
        
del notas[chave]
print(notas)