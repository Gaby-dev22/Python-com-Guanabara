# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Qual o seu nome completo? ')).strip()
primeiro_nome = nome.split()[0]  # Divide o nome nos espaços e pega só o primeiro
ultimo_nome = nome.split()[-1]   # o '-1' irá mostrar o ultimo item da lista 

print(f'Seu primeiro nome é {primeiro_nome}')
print(f'Seu último nome é {ultimo_nome}')




