# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import random

alu_1 = input('Nome: ')
alu_2 = input('Nome: ')
alu_3 = input('Nome: ')
alu_4 = input('Nome: ')
lista = [alu_1, alu_2, alu_3, alu_4] #Precisa ser em colchetes
escolhido = random.choice(lista) # Retorna um elemento aleatório da sequência

print(f'O aluno(a) escolhido foi: {escolhido}')