# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

n1 = input('Digite um número ente 0 e 9999: ')
n1 = n1.zfill(4) #completa com '0' a esquerda

print(f'unidade: {n1[3]}')
print(f'dezena: {n1[2]}')
print(f'centena: {n1[1]}')
print(f'milhar: {n1[0]}')
