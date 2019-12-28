while True:
    dec = int(input('Digite um numero inteiro : '))

    opcao = int(input('Escolha a base de conversão :\n 1-Bin\n 2-Hex\n 3-Oct '))

    if opcao == 1:
        bin = bin(dec)
        print(bin)
    elif opcao == 2:
        hex = hex(dec)
        print(hex)
    elif opcao == 3:
        oct = oct(dec)
        print(oct)
    else:
        print('Você não digitou um numero válido.')