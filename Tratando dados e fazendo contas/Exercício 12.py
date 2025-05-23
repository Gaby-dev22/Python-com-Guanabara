# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

preço_atual = float(input('Preço atual: '))
desconto = preço_atual * 0.05
preço_novo = preço_atual - desconto

print(f'O preço com 5% de desconto é {preço_novo} reais')