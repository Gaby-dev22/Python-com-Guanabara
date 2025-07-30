# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

#tentativa tranaformando o ultimo digito em string
numero = input("Digite um número: ")
ultimo_digito = numero[-1] # Isso ira verificar apenas o último caractere 

if ultimo_digito in '02468':  # Verifica se o último dígito é par
    print("É par")
else:
    print("É ímpar")

#jeito "certo"

numero = int(input('Me diga um número qualuer: '))
resultado = numero % 2
if resultado == 0:
    print(f'O número {numero} é PAR')
else:
    print(f'O número é {numero} ÍMPAR')