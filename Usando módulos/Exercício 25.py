# Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nome = str(input('Seu nome: ')).strip()

print(f'Seu nomep tem Silva? {'SILVA' in nome.upper()} ')