# Escreva um programa que leia a velocidade de um carro. 
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
# A multa vai custar R$7,00 por cada Km acima do limite

#tentativa errado
#velocidade_limete = 80 
#velocimetro = float(input("Qual a velocidade: "))  
#if velocimetro <= velocidade_limete:
#    print("Tudo certo")
#else:
#    velocimetro > velocidade_limete
#    print(f"Este caro será multado em R$7,00, por alta velocidade {velocimetro} Km")

#correto

velocidade = float(input("Qual a velocidade: "))
if velocidade > 80:
    multa = (velocidade-80) * 7
    print(f"Multado, vc acedeu o limite de velocidade, deve pagar R${multa:.2f}")
print("Bom dia, dirija com segurança")
