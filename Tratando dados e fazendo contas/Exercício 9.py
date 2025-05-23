# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada

n1 = float(input('Escreva um número: '))

t1 = n1 * 1
t2 = n1 * 2
t3 = n1 * 3
t4 = n1 * 4
t5 = n1 * 5
t6 = n1 * 6
t7 = n1 * 7 
t8 = n1 * 8
t9 = n1 * 9
t10 = n1 * 10

print(f'A tabuada de {n1} é: \n {t1, t2, t3, t4, t5, t6, t7, t8, t9, t10} ')

#ou (melhor)

numero = int(input('Digite um número para a tabuada: '))
print(f'Tabuada do {numero}')
for i in range (1, 11): # 'range(1,11)'cria uma sequência de números de 1 a 10 ; 'i' váriavel que armazena o valor atual do loop 
    print(f'{numero} * {i} = {numero * i}')