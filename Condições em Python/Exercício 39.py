#  Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, 
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date 
ano_nascido = int(input('Ano de nascimento: '))
ano_atual = date.today().year
alistar = ano_atual - ano_nascido
if alistar == 18:
    print('Está no tempo para se alistar')
elif alistar < 18:
    ano_falta = 18 - alistar
    print(f'Falta {ano_falta} anos para se alistar')
    ano_alistar = ano_atual + ano_falta
    print(f'Seu alistamento será em {ano_alistar}')
elif alistar > 18:
    ano_passou = alistar - 18
    print(f'Já passou {ano_passou} anos para vc se alistar')
    ano_alistar = ano_atual - ano_passou
    print(f'Seu alistamento foi em {ano_alistar}')