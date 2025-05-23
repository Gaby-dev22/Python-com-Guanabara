# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
# Ex: Digite um número: 6.127
# O número 6.127 tem a parte Inteira 6.

import math

num = float(input('Digite um número para ver sua porção inteira: '))
inteiro = math.trunc(num) # Retorna 'num' com a parte fracionária removida, deixando a parte inteira

print(f'A porção inteira de {num} é {inteiro}')