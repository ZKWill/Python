s = 0
for c in range(1, 11):
    num = int(input(f'Insira o {c}º número: '))
    s += num
print(f'A média dos números inseridos é {s/10:.2f}')
