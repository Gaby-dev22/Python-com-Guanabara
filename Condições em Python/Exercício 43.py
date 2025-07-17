# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) 
# e mostre seu status, de acordo com a tabela abaixo: – IMC abaixo de 18,5: Abaixo do Peso; – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso; – 30 até 40: Obesidade; – Acima de 40: Obesidade Mórbida

altura = float(input('Qual a sua altura(m):  ').replace(',','.')) # Converte a vírgula para ponto antes de transformar em float
peso = float(input('Qual o seu peso(Kg): ').replace(',','.'))
imc = peso / (altura**2) # Eleva ao quadrado

if imc <= (185/10):
    print(f'Seu IMC é {imc:.1f}. Você está ABAIXO DO PESO')
elif (185/10) <= imc < 25:
    print(f'Seu IMC é {imc:.1f}. Você está no PESO IDEAL ')
elif 25 <= imc < 30:
    print(f'Seu IMC é {imc:.1f}. Você está com SOBREPESO')
elif 30 <= imc < 40:
    print(f'Seu IMC é {imc:.1f}. Você está com OBESIDADE')
else:
    print(f'Seu IMC é {imc:.1f}. Você está com OBESIDADE MÓRBIDA')
