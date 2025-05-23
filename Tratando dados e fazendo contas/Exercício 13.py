# Faça um algoritmo que leia o sálario de um funcionário e mostra seu novo salário, com 15% de aumento. 

salario = float(input('Qual o sálario? '))
aumento = int(input('Quanto deseja de aumento? '))
novo_salario = (aumento / 100) * salario + salario


print(f'Sálario com {aumento}% de aumento é {novo_salario}')