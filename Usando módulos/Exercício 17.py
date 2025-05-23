# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. 
# Calcule e mostre o comprimento da hipotenusa.
import math

cat_o = float(input('Qual o comprimento do cateto oposto: '))
cat_ad = float(input('Qual o compimento do catetto adjacente: '))
hipo = math.hypot(cat_o, cat_ad)

print(f'A hipotenusa de {cat_o} e {cat_ad} é {hipo:.2f}')