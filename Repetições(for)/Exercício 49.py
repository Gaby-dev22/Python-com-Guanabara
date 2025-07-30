# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

numero = int(input('Digite um número: '))
print(f'Tabuada do {numero}')
for t in range(0,11):
    resultado = t * numero
    print(f'{t} x {numero} = {resultado}')
