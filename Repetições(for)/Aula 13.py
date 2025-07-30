for c in range(1,6): # Contagem de 1 á 5(igonora último número)
    print('Oi')
print('FIM')

for c in range(0,6): # Contagem de 1 á 6
    print('Oi')
print('FIM')

for c in range(0,6): # Contagem 6 vezes do oi e Fim
    print('Oi')
    print('FIM')

for c in range (0,6):
    print(c) # Contagem de 1 até 5
print('FIM')

for c in range(6,0): # Só aparecera o 'FIM'
    print(c)
print('FIM')

for c in range(6,0,-1): # Contara de trás pra frente
    print('c')
print('FIM')

for c in range(0,7,2): # Contará de 2 em 2
    print(c)
print('FIM')

i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i,f+1,p):
    print(c)
print('FIM!')

b = 0
for c in range(0,3):
    a = int(input('Digite um valor: '))
    b += a
print(f'A soma de todos os valores é {b}')
print('FIM')