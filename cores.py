# código de style 0 = fonte normal
# código de style 1 = fonte em negrito
# código de style 4 = fonte sublinhada
# código de style 7 = fonte 'negativa'

# código de text 30 = letra branca
# código de text 31 = letra vermelha
# código de text 32 = letra verde
# código de text 33 = letra amarela
# código de text 34 = letra azul
# código de text 35 = letra lilás
# código de text 36 = letra ciano
# código de text 37 = letra cinza

# código de back 40 = fundo branco
# código de back 41 = fundo vermelho
# código de back 42 = fundo verde
# código de back 43 = fundo amarelo
# código de back 44 = fundo azul
# código de back 45 = fundo lilás
# código de back 46 = fundo ciano
# código de back 47 = fundo cinza

# syntax \033[0;33;44m
# em primeiro vem a fonte, depois cor da letra e depois cor do fundo
print('\033[1;33;42mOlá mundo!\033[m')
print('\033[1;33;43mOlá mundo!\033[m')
