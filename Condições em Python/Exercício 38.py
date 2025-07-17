# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#– O primeiro valor é maior
#– O segundo valor é maior
# Não existe valor maior, os dois são iguais

print('-=-'*20)
n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))

if n1 > n2:
    print(f'O primeiro valor maior é {n1}')
    print(f'O segundo valor maior é {n2}') 
elif n1 < n2:
    print(f'O primeiro valor maior é {n2}')
    print(f'O segundo valor maior é {n1}')
else:
    print('Os valores são iguais')