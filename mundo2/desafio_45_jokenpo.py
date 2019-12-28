from random import randint
import time

dados = {1: 'pedra', 2: 'papel', 3: 'tesoura', 4: 'SAIR'}
jogador_winners = 0
comp_winners = 0
continuar = True
while continuar == True:
    print('---Inicio do Jogo JOKENPÔ---\n')

    for k, v in dados.items():
        print(f'\t{k} : {v.upper()}')

    opcao_computador = randint(1, 3)
    opcao_jogador = int(input('Escolha a opção desejada: '))

    if opcao_jogador > 4 or opcao_jogador < 1:
        print('Opção invalida. Digite novamente')
    elif opcao_jogador == 4:
        continuar = False
        break
    print('JO')
    time.sleep(1)
    print('KEN')
    time.sleep(1)
    print('PÔ!!!')
    print('=-' * 11)

    jogador = dados[opcao_jogador]
    computador = dados[opcao_computador]

    if jogador == computador:
        print('EMPATOU')
    elif opcao_jogador == 1 and opcao_computador == 2:
        print(f'Perdeu! {computador} ganha de {jogador}')
        comp_winners += 1
    elif opcao_jogador == 1 and opcao_computador == 3:
        print(f'Ganhou! {jogador} ganha de {computador}')
        jogador_winners += 1
    elif opcao_jogador == 2 and opcao_computador == 3:
        print(f'Perdeu! {computador} ganha de {jogador}')
        comp_winners += 1
    elif opcao_jogador == 2 and opcao_computador == 1:
        print(f'Ganhou! {jogador} ganha de {computador}')
        jogador_winners += 1
    elif opcao_jogador == 3 and opcao_computador == 1:
        print(f'Perdeu! {computador} ganha de {jogador}')
        comp_winners += 1
    elif opcao_jogador == 3 and opcao_computador == 2:
        print(f'Ganhou! {jogador} ganha de {computador}')
        jogador_winners += 1
    else:
        print('FODEU!')

    print('---' *10)
    print(f'PLACAR DA RODADA : JOGADOR {jogador_winners} || COMPUTADOR {comp_winners}')
    print('---' * 10)

    if(jogador_winners == 5 and comp_winners < 5):
        print('PARABENS! VC GANHOU A DISPUTA!!')
        continuar = False
        break
    elif(comp_winners ==5 and jogador_winners < 5):
        print('SHAME! VC PERDEU A DISPUTA!!')
        continuar = False
        break