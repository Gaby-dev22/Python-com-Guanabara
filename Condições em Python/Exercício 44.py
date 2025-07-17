# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#– à vista dinheiro/cheque: 10% de desconto; – à vista no cartão: 5% de desconto; – em até 2x no cartão: preço formal 
#– 3x ou mais no cartão: 20% de juros

produto = float(input('Valor das compras:R$ '))
pagamento = int(input(''' Formas de pagamento:
[1] Dinheiro desconto em 10% 
[2] Cartão desconto em 5%
[3] Parcelado em 2x valor normal
[4] Parcelado em 3x ou mais juros em 20%
Opção: '''))

if pagamento == 1: 
    dinheiro = produto - (produto * (10/100))
    print(f'O R${produto} tem 10% de desconto, pagando em dinheiro fica R${dinheiro:.2f}')
elif pagamento == 2: 
    cartao = produto - (produto * (5/100))
    print(f'O R${produto} tem 5% de desconto, pagando à vista no cartão fica R${cartao:.2f}')
elif pagamento == 3:
    parcela = produto / 2
    print(f'O R${produto} sem juros em 2x no cartão com parcelas de R${parcela:.2f} cada')
elif pagamento == 4:
    parcelas = int(input('Em quantas vezes: '))
    parcelado_x = produto + (produto * (20/100))
    parcela = parcelado_x / parcelas
    print(f'O R${produto} fica em {parcelado_x:.2f} parcelado com 20% de juros com R${parcela:.2f} cada')
else:
    print('Tente novamente. Escolha alguma das alternativas')