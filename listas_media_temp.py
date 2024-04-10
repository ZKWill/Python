soma = 0
media = 0
temperaturas = [28.5 , 33.5, 33.1, 30.9, 26.3, 26.7, 25.5, 28.2, 22.6, 34.0, 25.1, 33.5]

for c in temperaturas:
    soma += c
media = soma / 12
print(f'A média de temperatura do ano de 2022 foi de {media:.1f}ºC')

for m, c in enumerate(temperaturas):
    if c >= media:
        if m == 0:
            print(f'O mês de Janeiro ultrapassou a temperatura média do ano, com {c}ºC')
        if m == 1:
            print(f'O mês de Fevereiro ultrapassou a temperatura média do ano, com {c}ºC')
        if m == 2:
            print(f'O mês de Março ultrapassou a temperatura média do ano, com {c}ºC')
        if m == 3:
            print(f'O mês de Abril ultrapassou a temperatura média do ano, com {c}ºC')
        if m == 4:
            print(f'O mês de Maio ultrapassou a temperatura média do ano, com {c}ºC')
        if m == 5:
            print(f'O mês de Junho ultrapassou a temperatura média do ano, com {c}ºC')
        if m == 6:
            print(f'O mês de Julho ultrapassou a temperatura média do ano, com {c}ºC')
        if m == 7:
            print(f'O mês de Agosto ultrapassou a temperatura média do ano, com {c}ºC')
        if m == 8:
            print(f'O mês de Setembro ultrapassou a temperatura média do ano, com {c}ºC')
        if m == 9:
            print(f'O mês de Outubro ultrapassou a temperatura média do ano, com {c}ºC')
        if m == 10:
            print(f'O mês de Novembro ultrapassou a temperatura média do ano, com {c}ºC')
        if m == 11:
            print(f'O mês de Dezembro ultrapassou a temperatura média do ano, com {c}ºC')