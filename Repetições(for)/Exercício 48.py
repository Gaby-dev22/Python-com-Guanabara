# Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
soma = 0
for cal in range(0,501):
    if cal % 3 == 0:
        soma += cal # soma = cal + soma, necessário ter a variavel 'soma = 0'
        print(cal)
print(f'A soma é {soma}')
    

