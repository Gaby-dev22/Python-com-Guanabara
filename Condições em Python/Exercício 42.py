# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais; – ISÓSCELES: dois lados iguais, um diferente; – ESCALENO: todos os lados diferentes

reta_1 = float(input('Qual o comprimento da primeira reta? '))
reta_2 = float(input('Qual o comprimento da segunda reta? '))
reta_3 = float(input('Qual o comprimento da terceira reta? '))
triangulo = reta_1 < reta_2 + reta_3 and reta_2 < reta_1 + reta_3 and reta_3 < reta_1 + reta_2

# Testa se pode formar um triângulo
if triangulo:
    print('Os valores acima podem formar um triângulo')
    if triangulo and reta_1 == reta_2 == reta_3:
        print('É EQUILÁTERO')       
elif triangulo and reta_1 != reta_2 == reta_3 or reta_1 != reta_3 == reta_2 or reta_2 != reta_3 == reta_1: # otimizado: (reta_1 == reta_2) or (reta_1 == reta_3) or (reta_2 == reta_3)
        print('É ISÓSCELES')
elif triangulo and reta_1 != reta_2 != reta_3 and reta_2 != reta_1 != reta_3 and reta_1 != reta_3 != reta_2: # otimizado: reta_1 != reta_2 and reta_1 != reta_3 and reta_2 != reta_3
        print('É ESCALENO')
else:
    print('Os valores acima NÃO podem formar um triângulo')


