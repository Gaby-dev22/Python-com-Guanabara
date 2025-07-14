# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))

#maior

if n1 > n2 and n1 > n3:
    print(f'{n1} é o maior número')
elif n2 > n1 and n2 > n3:
    print(f'{n2} é o maior número')
elif n3 > n1 and n3 > n1: 
    print(f'{n3} é o maior número')

# menor

if n1 < n2 and n1 < n3:
    print(f'{n1} é o menor número')
elif n2 < n1 and n2 < n3:
    print(f'{n2} é o menor número')
else:
    print(f'{n3} é menor número')

#repetidos ou iguais

if n1 == n2 == n3:
    print('Todos os números são iguais')
elif n1 == n2 or n1 == n3 or n2 == n3:
    print('Há números repetidos')
