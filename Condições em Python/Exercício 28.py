# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir 
# qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
computador = randint(0,5) # Faz o computador sorter entre 0 e 5
print('-=-'*20)
print('Tente advinha o número que eu pensar')
print('-=-'*20)

jogador = int(input('Em que número pensei: '))
if jogador == computador:
    print('Parabéns vc acertou')
else:
    print(f'Vc errou perdedor, eu pensei no numero {computador}')
