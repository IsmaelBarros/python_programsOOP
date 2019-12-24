from banco.banco import Banco
from banco.contapoupanca import ContaPoupanca
from banco.contacorrente import ContaCorrente
from pessoas.cliente import Cliente

banco = Banco()

cliente1 = Cliente('Maira', 31)

cliente2 = Cliente('Ismael', 34)
conta1 = ContaPoupanca(1111, 2677, 0)
conta2 = ContaCorrente(2222, 3465, 0)
cliente1.inserir_conta(conta1)
cliente2.inserir_conta(conta2)

banco.inserir_cliente(cliente1)
banco.inserir_conta(conta1)

banco.inserir_cliente(cliente2)
banco.inserir_conta(conta2)

if banco.autenticar(cliente2):
    cliente1.conta.depositar(850)
    cliente1.conta.sacar(100)
else:
    print('Cliente não autenticado.')
