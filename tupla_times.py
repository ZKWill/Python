times = ('Botafogo', 'Grêmio', 'Palmeiras', 'Bragantino', 'Flamengo', 'Atlético-MG', 'Athletico-PR', 'Fluminense', 'São Paulo', 'Cuianá', 'Fortaleza', 'Internacional', 'Santos', 'Corinthians', 'Bahia', 'Vasco da Gama', 'Cruzeiro', 'Goiás', 'Coritiba', 'América-MG')
print(f'Esses são os 5 primeiros colocados do Brasileirão {times[:5]}')
print(f'Esses são so 4 últimos colocados do Brasileirão {times[16:]}')
print(sorted(times))
for n, t in enumerate(times):
    if t == 'Internacional':
        print(f'O Internacional está na {n + 1}º posição')