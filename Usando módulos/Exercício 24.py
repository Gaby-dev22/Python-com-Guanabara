# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cidade = input('Nome de cidade: ').strip()

print(cidade[:5].upper() == 'SANTO')