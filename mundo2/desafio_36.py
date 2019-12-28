preco_imovel = float(input('Informe o valor da casa : '))
salario = float(input('Informe seu salario mensal : '))
tempo = float(input('Informe quantos anos para o financiamento : '))


def calculo_parcelas():

    valor_parcela = preco_imovel / (tempo*12)

    if valor_parcela > (salario * 30/100):
        print('Financiamento negado, parcela supera 30% do seu salario mensal')
        print(f'Você recebe R${salario:.2f} e as parcelas de R${valor_parcela:.2f}')
        return False
    else:
        print('Financiamento aprovado!')
        print(f'Você recebe R${salario:.2f} e as parcelas de R${valor_parcela:.2f}')
        return True


print(calculo_parcelas())