# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, 
#de acordo com a média atingida: – Média abaixo de 5.0: REPROVADO; – Média entre 5.0 e 6.9: RECUPERAÇÃO; – Média 7.0 ou superior: APROVADO

nota1 = float(input('Digite a sua nota: '))
nota2 = float(input('Digite sua outra nota: '))
media = (nota1 + nota2) / 2

if media < 5:
    print(f'A sua média é {media}. Você está REPROVADO')
elif 5 <= media <= 6.9:
    print(f'A sua média foi {media}. Você está de RECUPERAÇÃO')
else:
    print(f'A sua média é {media}. Você está APROVADO')
