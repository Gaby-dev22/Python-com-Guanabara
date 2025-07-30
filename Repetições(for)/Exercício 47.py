# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50

for par in range(1,51):  
    if par % 2 == 0:    # O resto da divisão entre 1 e 51 que for 0, será um número par 
        print(par)

# Outra forma 

for par in range(2,51,2):
    print(par)
