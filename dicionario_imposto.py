paises = {'Malta' : 35, 'Brasil' : 34, 'Namibia' : 32, 'Portugal' : 32, 'Colombia' : 30, 'Argentina' : 30, 'Austrália' : 30, 'Rep. Congo' : 30, 'Costa Rica' : 30, 'Gabão' : 30}

for i in paises:
    if paises[i] > 30:
        print(i, paises[i])
    
paises['Paraguai'] = 10
print(paises)