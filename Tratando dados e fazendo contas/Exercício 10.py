# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira a mostra quantos dólares ela pode comprar. Considerar US$1,00 = R$3,27

carteira = int(input('Saldo da carteira?: R$ '))
dolar = carteira / 3,27

print(f'Com R$ {carteira:.2f} compra até U$ {dolar[0]:.2f} dólares') # a variavel 'dolar' por ser <class 'tuple'>, usa o '[0]' para converter em um número, pois a formatação de string ':.2f' não funcionaria