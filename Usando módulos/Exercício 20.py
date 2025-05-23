# O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. 
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

alu_1 = input('Priemiro grupo: ')
alu_2 = input('Segundo grupo: ')
alu_3 = input('Terceiro grupo: ')
alu_4 = input('Quarto grupo: ')
lista = [alu_1, alu_2, alu_3, alu_4]
ordem = random.sample(lista, k=len(lista))

print(f'Ordem de apresentação é {ordem}')