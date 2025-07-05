# Desenvolva um programa que pergunte a distância de uma viagem em Km. 
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e 
# R$0,45 parta viagens mais longas.

distancia = int(input('Quantos Km deseja viajar? '))

if distancia < 201:
    viagem_1 = 50 / 100
    viagem_curta = distancia * viagem_1
    print(f'A passagem será R${viagem_curta}')
else:
    viagem_2 = 45 / 100
    viagem_longa = distancia * viagem_2
    print(f'A passagem será R${viagem_longa}')

