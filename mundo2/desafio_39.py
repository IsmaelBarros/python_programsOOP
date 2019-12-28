from datetime import datetime

ano_nasc = int(input('Digite seu ano de nascimento /0000: '))

ano_atual = datetime.now()

idade = ano_atual.year - ano_nasc

if idade < 17:
    tempo_restante = 17 - idade
    print(f'Você não precisa se alistar. Falta(m) {tempo_restante} ano(s).')
elif idade > 17:
    tempo_excedido = idade - 17
    print(f'Passou {tempo_excedido} ano(s) para seu alistamento.')
else:
    print(f'Vc tem {idade} anos e  precisa se alistar.')
