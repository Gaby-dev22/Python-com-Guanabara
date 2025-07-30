#  Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 
# 1 para binário, 2 para octal e 3 para hexadecimal.
print('///'*20)
numero = int(input('Qual número quer converter? '))
print('///'*20)
print('''Escolha uma das bases para conversão
[1] Binário
[2] Octal
[3] Hexadecimal ''')
opçao = int(input('Escolha uma das bases para conversão: '))

if opçao == 1:
    print(f'O {numero} em binário é {bin(numero)[2:]}') # o '[2:]' remove os 2 primeiros caracteres
elif opçao == 2:
    print(f'O {numero} em octal é {oct(numero)[2:]}')
elif opçao == 3:
    print(f'O {numero} em hexadecimal é {hex(numero)[2:]}')
else:
    print('Opção inválida. Tente novamente')