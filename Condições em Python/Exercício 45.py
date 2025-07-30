# Crie um programa que faça o computador jogar Jokenpô com você.

from random import choice
# Escolha do úsuario
escolha = int(input('''
1 - Pedra
2 - Papel
3 - Tesoura 
Escolha: ''')) 

print('JO')
print('KEN')
print('PÔ')
print('-=-'*20)

if 1 == escolha: 
    print('Você escolheu PEDRA')
elif 2 == escolha:
    print('Você escolheu PAPEL')
elif 3 == escolha:
    print('Você escolheu TESOURA')
else:
    print('Escolha uma das opções acima. Tente Novamente')

# Escolha do computador
computador = choice(['pedra', 'papel', 'tesoura'])
# Transformando as strings em números para comparação com úsuario
if computador == 'pedra':
    computador_num = 1     # Use UMA única variável para armazenar o resultado
elif computador == 'papel':
    computador_num = 2
elif computador == 'tesoura':
    computador_num = 3

print(f'Computador jogou {computador.upper()}')
print('-=-'*20)
# Comparação entre ganhadores

if escolha == computador_num:
    print('EMPATE')
elif escolha == 1 and computador_num == 2:
    print('VOCÊ GANHOU')
elif escolha == 1 and computador_num == 3:
    print('VOCÊ GANHOU') 
elif escolha == 2 and computador_num == 1:
    print('COMPUTADOR GANHOU')
elif escolha == 2 and computador_num == 3:
    print('COMPUTADOR GANHOU')
elif escolha == 3 and computador_num == 1:
    print('COMPUTADOR GANHOU')
elif escolha == 3 and computador_num == 2:
    print('VOCÊ GANHOU')
