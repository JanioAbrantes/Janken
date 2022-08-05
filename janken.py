"""
Apenas um joguinho de pedra, papel e tesoura
"""

from random import choice

pedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tesoura = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

janken = [pedra, papel, tesoura]
player_score = 0
machine_score = 0


def score(player, machine):
    global player_score
    global machine_score
    if (player == pedra and machine == tesoura) \
            or (player == papel and machine == pedra) \
            or (player == tesoura and machine == papel):
        player_score += 1
        print(f'PONTUAÇÃO ATUAL\nJogador: {player_score}\nMaquina: {machine_score}')

    elif (machine == pedra and player == tesoura) \
            or (machine == papel and player == pedra) \
            or (machine == tesoura and player == papel):
        machine_score += 1
        print(f'PONTUAÇÃO ATUAL\nJogador: {player_score}\nMaquina: {machine_score}')

    else:
        print('DRAW')
        jankenpo()

    if player_score == 2:
        print('Parabéns, você venceu. Nunca critiquei. Quer jogar de novo?')
        replay = input('Digite Y para sim ou qualquer outra tecla para não\n').strip().lower()
        if replay == 'y':
            print('Massa. Vamo lá mais uma vez')
            jankenpo()
        else:
            print('Adeus meu camarada')
            quit()

    elif machine_score == 2:
        print('Perdeu muleque. Quer ter uma revanche pra vê se perde de novo?')
        replay = input('Digite Y para sim ou qualquer outra tecla para não\n').strip().lower()
        if replay == 'y':
            print('Bom é assim. Tem que ser brasileiro e não desistir nunca')
            jankenpo()
        else:
            print('Arregão de merda. Vaitimbora carniça')
            quit()

    else:
        jankenpo()


def jankenpo():
    player = input('Escolha entre pedra, papel ou tesoura: ').strip().lower()
    machine = choice(janken)
    if player in ['pedra', 'papel', 'tesoura']:
        if player == 'pedra':
            player = pedra
            print(pedra)
            print(machine)
            score(player, machine)

        elif player == 'papel':
            player = papel
            print(papel)
            print(machine)
            score(player, machine)
        else:
            player = tesoura
            print(tesoura)
            print(machine)
            score(player, machine)
    else:
        print('Escolha inválida. Tente novamente')
        jankenpo()


print('Bem vindos ao Jan Ken Janio\nNesse jogo de pedra, papel e tesoura, vence quem tiver 2 vitórias primeiro\n')
print('JAN\n   KEN\n      PO\n')
jankenpo()
