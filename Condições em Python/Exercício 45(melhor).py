from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Opções: 
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Sua escolha: '))
print('JO')
print('KEN')
print('PÔ')
print('-=-'*11)
print(f'Jogador jogou {jogador}')
print(f'Computador jogou {computador}')
print('-=-'*11)

if computador == 0: # Computador jogou pedra
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('COMPUTADOR VENCEU')
    elif jogador == 2:
        print('COMPUTADOR VENCEU')
    else:
        print('Jogada Inválida')
elif computador == 1: # Computador jogou papel
    if jogador == 0:
        print('JOGADOR VENCEU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCEU')
    else:
        print('Jogada Inválida')
elif computador == 2: # Computador jogou tesoura
    if jogador == 0:
        print('JOGADOR VENCEU')
    elif jogador == 1:
        print('COMPUTADOR VENCEU')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Jogada Inválida')