# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado 
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, 
# sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

Km = float(input('Quanto o carro percorreu em Km: '))
d = int(input('Foi alugado por quantos dias: '))
preço = (d * 60) + (Km * 0.15)

print(f'O total a ser pago é R${preço}')
