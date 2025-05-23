# Crie um programa que leia o nome completo de uma pessoa e mostre:
# – O nome com todas as letras maiúsculas e minúsculas.
# – Quantas letras ao todo (sem considerar espaços).
# – Quantas letras tem o primeiro nome.

nome = str(input('Nome completo: ')).strip()  #Recebe nome e remove espaços extras
print('Analisando nome')
print(f'Seu nome em minúsculo é {nome.lower()}')  # Converte para minúsculas
print(f'Em maiúsculo: {nome.upper()}')            # Converte para maiúsculas
print(f'Seu nome tem: {len(nome) - nome.count(' ')} letras')  # Conta letras (excluindo espaços)
print(f'|O primeiro nome tem: {nome.find(' ')}')   # Mostra posição do primeiro espaço (tamanho do 1º nome)