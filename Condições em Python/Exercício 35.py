# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

reta_1 = float(input('Qual o comprimento da primeira reta? '))
reta_2 = float(input('Qual o comprimento da segunda reta? '))
reta_3 = float(input('Qual o comprimento da terceira reta? '))

if reta_1 < reta_2 + reta_3 and reta_2 < reta_1 + reta_3 and reta_3 < reta_1 + reta_2:
    print('Os valores acima podem formar um triângulo')
else:
    print('Os valores acima NÃO podem formar um triângulo')
