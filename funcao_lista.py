lista = [10, 1, 4, 8, 5, 2, 9, 7, 3 ]

print(f'A lista original é {lista}\n')
def controle(lista):
    lista_ordenada = sorted(lista)
    return lista_ordenada

print(f'A lista arrumada ficará {controle(lista)}')