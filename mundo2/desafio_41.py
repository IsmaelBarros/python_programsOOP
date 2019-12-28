from datetime import datetime

ano_nasc = int(input('Informe seu ano de nascimento (/0000): '))

ano_atual = datetime.now()
idade = ano_atual.year - ano_nasc

if(idade <= 9):
    print('categoria MIRIM')
elif(idade > 9 and idade <= 14):
    print('categoria INFATIL')
elif(idade > 14 and idade <= 19):
    print('categoria JUNIOR')
elif(idade > 19 and idade <= 20):
    print('categoria SENIOR')
else:
    print('categoria MASTER')

if idade:
    print('Oi')
