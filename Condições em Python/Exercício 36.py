# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

print('-=-'*20)
casa = float(input('Qual o valor da casa: '))
print('-=-'*20)
salario = float(input('O seu salário: '))
print('-=-'*20)
tempo = float(input('Em quantos anos irá pagar? '))
print('-=-'*20)
prestação = casa / (tempo * 12)
minimo = (30/100) * salario

if prestação <= minimo:
    print('O empréstimo está liberado')
else:
    print('Você não possui renda mensal o suficiente') 