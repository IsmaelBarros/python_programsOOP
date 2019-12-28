nota1 = float(input('informe a primeira nota: '))
nota2 = float(input('informe a segunda nota: '))

media = (nota1+nota2) /2
print()
if media >= 7.0:
    print('APROVADO\n')
    print(f'Sua média foi de {media}')
if media >= 5.0 and media < 7.0:
    print('RECUPERACAO\n')
    print(f'Sua média foi de {media}')
else:
    print('REPROVADO\n')
    print(f'Sua média foi de {media}')