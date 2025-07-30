# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

numero = int(input('Digite um número para saber sua PA: ')) 
razao = int(input('E a razão: '))
termo_atual = numero
print('Os 10 primeiros termos são: ')

for i in range(10):
    print(termo_atual, end='-> ')
    termo_atual = termo_atual + razao