n1 = int(input('Digite o primeiro número : '))
n2 = int(input('Digite o segundo número : '))

if n1 > n2:
    print(f'O {n1} é maior que {n2}')
elif n1 < n2:
    print(f'O {n1} é menor que {n2}')
else:
    print(f'O {n1} é igual ao {n2}')