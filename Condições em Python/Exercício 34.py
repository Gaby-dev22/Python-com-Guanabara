# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
# Para salários superiores a R$1250,00, calcule um aumento de 10%. 
# Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Qual o seu salário? '))

if salario > 1250:
    aumento_1 = salario * (10/100)
    novo_salario = salario + aumento_1
    print(f'Seu novo salário é {novo_salario:.2f}')
elif salario <= 1250:
    aumento_2 = salario * (15/100)
    novo_salario = salario + aumento_2
    print(f'Seu novo salário é {novo_salario:.2f}') 

# código otimizado

salario = float(input("Qual o seu salário? "))

if salario<= 1250:
    novo = salario + (salario * 15/100)
else:
    novo = salario + (salario * 10/100)
print(f'Quem recebia R${salario:.2f}, passa a ser R${novo:.2f}')