'''Protótipo inicial do sistema de Texas Hond'em. O programa tem que:
1. Receber a posição na mesa
2. Receber as cartas iniciais da mão
3. Mostrar a probabilidade de cada tipo de mão
4. Receber as cartas que saíram na mesa
5. Mostarar probvabilidade atualizada de cada tipo de mão
6. Receber a penúntima carta
7. Mostrar estatística atualizada
8. Receber a última carta
9.Atualizar por últioma vez a estatística, mostrando qual mão formou'''

from Hands import *

'''players = int(input('Quantos jogadores estão na mesa? '))
rounds = list(range(players))
position = int(input(f'Qual a sua posição na mesa [de 0 à {len(rounds)-1}]?'))'''


#Lista da mão inicial
pre_flop = result(cards_list(2))
print(pre_flop)


#Dicionário do flop
flop = result(cards_list(3))
print(flop)


#Dicionário do Turn
turn = result(cards_list(1))
print(turn)


#Dicionário do River
river = result(cards_list(1))
print(river)


