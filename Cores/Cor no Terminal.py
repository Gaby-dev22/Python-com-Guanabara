# Utilizar os códigos de escape sequence ANSI para configurar cores no python
# Pelo código \033[ m...\033[m
# Style: 0,1,4,7
# Text: 30 á 37
# Back: 40 á 47

print('\033[1;31;43mHello, Word!\033[m')

print('\033[7;37;45mHello, Word!\033[m')

print('\033[37mHello, Word!\033[m')

a = input('Qualquer coisa: ')
b = input('Qualquer coisa: ')
print(f'Primeiro \033[32m{a} e \033[31m{b}')