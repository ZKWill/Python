sup50 = 0
totalt = 0
altmed = 0
inf = 0
for c in range(1, 6):
    peso = float(input(f'Insira o peso da {c}º pessoa: '))
    altura = float(input(f'Insira a altura da {c}º pessoa: '))
    idade = int(input(f'Insira a idade da {c}º pessoa: '))
    if idade > 50:
        sup50 += 1
    if 10 < idade < 20:
        totalt += altura
        altmed += 1
    if peso < 60:
        inf += 1
print(f'Temos {sup50} pessoa(s) no grupo com idade superior a 50 anos')
print(f'A média de altura das pessoas entre 10-20 anos é de {totalt/altmed:.2f}')
print(f'A porcentagem de pessoas com peso inferior a 60Kg no grupo é de {inf*20}%')
