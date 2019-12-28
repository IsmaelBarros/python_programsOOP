dados = {1: ('à vista/dinheiro', '10%', 90.0),
         2: ('à vista/cartão', '5%', 95.0),
         3: ('parcelado até 2x', 'preço normal', 100.0),
         4: ('parcelado 3x ou mais', '20%', 120.0)
        }

for k, v in dados.items():
    if k == 3:
        print(f'{k} - {v[0]}, {v[1]}')
    elif k == 4:
        print(f'{k} - {v[0]}, juros de {v[1]}')
    else:
        print(f'{k} - {v[0]}, desconto de {v[1]}')

prod_preco = float(input('Informe o valor do produto: '))
pg = int(input('Digite a opção de pagamento: '))

preco_normal = prod_preco
ajuste = dados[pg][2]
preco_novo = preco_normal * ajuste/100

print(f'O preco antigo R${preco_normal}. Preço atualizado {preco_novo}')




