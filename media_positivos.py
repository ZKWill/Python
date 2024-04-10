s = 0
c = 0
num = 10
while c < num:
    n = int(input('Digite um número: '))
    if n > 0:
        s += n
    if n < 0:
        c -= 1
    c += 1
print(f'A média dos valores será {s / 10:.2f}')