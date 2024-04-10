def podesernum(num):
    try:
        int(num)
        return True
    
    except ValueError:
        return False

n = 0
arquivo = open('ex2.txt', 'r')
lista = arquivo.readlines()

# transforma a lista em str
palavras = ''.join(lista)
palavras_r = palavras.replace('-', '')
palavras_s = palavras_r.split()

lista_separada = [[], [], []]
lista_numeros = []

# um for que irá adicionar o valor do index (i) da lista palavras_s em uma lista dentro da lista (lista_separada)
for i in range (len(palavras_s)):
    lista_separada[n].append(palavras_s[i])
    if len(lista_separada[n]) > 1:
        n += 1

# verifica se o valor pode ser um número ou não
for num in palavras_s:
    if podesernum(num) == True:
        lista_numeros.append(int(num))

# ordena a lista em orden decrescente e em seguida transforma a lista int em uma lista de str
lista_numeros.sort(reverse= True)
lista_numeros = list(map(str, lista_numeros))

# verifica se um dos números está na lista, caso esteja ele irá imprimir ele na tela, indepente da posição em que estjea
for p in range (len(lista_numeros)):
    for i in range (len(lista_separada)):
        if lista_numeros[p] in lista_separada[i]:
            print(lista_separada[i])