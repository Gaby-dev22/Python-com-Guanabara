# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ela.

x = input('Digite algo: ')
print(f'Tipo: {type(x)}')
print(f'É alfabético? {x.isalpha()}')
print(f'É número? {x.isdigit()}')
print(f'É número ou letra? {x.isalnum()}')
print(f'É espaço? {x.isspace()}')
print(f'As letras são maiúsculas? {x.isupper()}')
print(f'As letras são minúsculas? {x.islower()}')
print(f'A formatão é de título? {x.title()}')
print(f'Os números são decimais? {x.isdecimal()}')
print(f'Apenas caracteres númericos? {x.isnumeric()}')