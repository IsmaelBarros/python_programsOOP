print("ESCOLHA A CERVEJA PELO NUMERO : ")
print("1-ANTARTICA R$6.00\n2-SKOL R$6.50\n3-BRAHMA R$8.20\n4-SOL R$8.25")
cerveja = input("5-NORTENHA R$16.80\n6-PROIBIDA R$4.80\n7-DEVASSA R$5.9\n8-HEINEKEN R$9.00")

q = float(input("Quantas ???"))

if cerveja == '1':
    valor_cerveja = 6 * q
    nome = "Antartica"
elif cerveja == '2':
    valor_cerveja = 6.5 * q
    nome = "Skol"
elif cerveja == '3':
    valor_cerveja = 8.2 * q
    nome = "Brahma"
elif cerveja == '4':
    valor_cerveja = 8.25 * q
    nome = "Sol"
elif cerveja == '5':
    valor_cerveja = 16.8 * q
    nome = "Nortenha"
elif cerveja == '6':
    valor_cerveja = 4.8 * q
    nome = "Proibida"
elif cerveja == '7':
    valor_cerveja = 5.9 * q
    nome = "Devassa"
elif cerveja == '8':
    valor_cerveja = 9 * q
    nome = "Heineken"
else:
    print("Valor invalido")

print(f'{nome} custa R${valor_cerveja} por {q} "cerveja(s)')