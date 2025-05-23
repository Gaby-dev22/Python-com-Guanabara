# Faça um programa que leia a largura e a altura de uma parede em metros. 
# Calcule a sua área e a quantidade de tinta necessária para pintá-la sabendo que cada litro de tinta, pinta uma área de 2m².

largura = float(input('Qual a largura da parede em m: '))
altura = float(input('Qual a altura da parede em m: '))
area = largura * altura
tinta = area // 2

print(f'Precisa de {tinta} litros')