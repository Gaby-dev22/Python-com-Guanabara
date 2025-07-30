# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

import math # Importa a biblioteca matemática

n1 = int(input('Digite um número: '))
dobro = n1 ** 2 
triplo = n1 ** 3 
raiz_quadrada = math.sqrt(n1) # Usa a função sqrt() do modulo math

print(f'dobro é {dobro}, triplo: {triplo}, raiz quadrada: {raiz_quadrada}')