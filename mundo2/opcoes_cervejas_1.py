dados = {1: ('ANTARTICA', 6.00), 2: ('SKOL', 6.50), 3: ('BRAHMA', 8.20), 4: ('SOL', 8.25),
         5: ('NORTENHA', 16.80), 6: ('PROIBIDA', 4.80), 7: ('DEVASSA', 5.90), 8: ('HEINEKEN', 9.00)
}

# print(dados.get(1))

print("ESCOLHA A CERVEJA PELO NUMERO : ")

for opcao in sorted(dados):
    #print("{} - {} (R$ {:.02f})".format(opcao, dados[opcao][0], dados[opcao][1]))
    print(f'{opcao} - {dados[opcao][0]} (R$ {dados[opcao][1]:.02f})')

cerveja = int(input("Opção desejada: "))

qtd = int(input('Quantidade: '))
nome = dados[cerveja][0]
preco = dados[cerveja][1]
total = qtd * preco

if qtd == 1:
    plural =''
else:
    plural = 's'

print(f"{nome} custa R${total} por {qtd} cerveja{plural}")
