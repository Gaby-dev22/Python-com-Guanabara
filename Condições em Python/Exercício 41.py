# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta 
# e mostre sua categoria, de acordo com a idade: – Até 9 anos: MIRIM; – Até 14 anos: INFANTIL; – Até 19 anos: JÚNIOR
#– Até 25 anos: SÊNIOR; – Acima de 25 anos: MASTER

from datetime import date
nascimento = int(input('Ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - nascimento

if 9 <= idade <= 13:
    print(f'Com {idade} anos você é atleta MIRIM')
elif 14 <= idade <= 18:
    print(f'Com {idade} anos você é atleta INFANTIL')
elif 19 <= idade <= 24:
    print(f'Com {idade} anos você é atleta JÚNIOR')
elif idade == 25:
    print(f'Com {idade} anos você é atleta SÊNIOR')
else:
    print(f'Com {idade} você é atleta MASTER')