# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

angulo = float(input('Digite um ângulo: '))
sen = math.sin(math.radians(angulo)) # converte o angulo para radianos para ser calculado corretamente
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))

print(f'O ângulo {angulo}° possui o seno {sen:.3f}°, coseno {cos:.3f}° e tangente {tan:.3f}°')