# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a 
# primeira vez e em que posição ela aparece a última vez.

frase = str(input('Diga uma frase: ')).strip().lower() # .lower = deixa tudo minúsculo
primeiro_a = frase.find('a') # primeira posição
ultimo_a = frase.rfind('a') # Última posição

print(f'Seu nome tem {frase.count('a')} as')
print(f'O priemrio a aparece: {primeiro_a}')
print(f'O último aparece: {ultimo_a}')
