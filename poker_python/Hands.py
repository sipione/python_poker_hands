from collections import Counter
import re
ranks = []
suits = []

#cria dicionários com as cartas
def cards_list(volume):
    ranks = []
    suits = []
    for i in range(0, volume):
        rank = int(input(f'Qual o valor da {i + 1}ª carta? '))
        ranks.append(rank)
        suit = input('Qual o nipe da carta? ')
        suits.append(suit)
    list = [ranks, suits]
    return list

def result(list):
    ranks.extend(list[0])
    suits.extend(list[1])
    result = _analyze(ranks, suits)
    return result

#Função de análise dos valores
def _analyze(rank_list, suits_list):
    if royal_flush(rank_list, suits_list):
        return f'Royal flush'
    elif four_kind(rank_list):
        return f'Four of a kind'
    elif straight_flush(rank_list, suits_list):
        return f'Straight flush'
    elif fullhouse(rank_list):
        return 'fullhouse'
    elif straight(rank_list):
        return f'straight'
    elif flush(suits_list):
        return 'flush'
    elif three_kind(rank_list):
        return 'three of a kind'
    elif two_pairs(rank_list):
        return 'two pairs'
    elif pair(rank_list):
        return 'a pair'


def royal_flush(rank_list, suits_list):
    if flush(suits_list):

        # make a copy to protect my global list
        provisory_ranks = rank_list[:]
        provisory_suits = suits_list[:]

        # findout the suit
        for i in Counter(provisory_suits).items():
            if i[1] < 5:

                # remove all the elements
                while i[0] in provisory_suits:
                    pos = provisory_suits.index(i[0])
                    provisory_suits.remove(i[0])
                    provisory_ranks.remove(provisory_ranks[pos])
        if {1, 10, 11, 12, 13} & set(provisory_ranks):
            return True
        else:
            return False
    else:
        return False

def four_kind(rank_list):
    for i in range(1, 14):
        if i in rank_list and rank_list.count(i) == 4:
            return True
    else:
        return False

def straight_flush(rank_list, suits_list):
    # only starts all loops and analizys if the others simpler are true
    if straight(rank_list) and flush(suits_list):

        #make a copy to protect my global list
        provisory_ranks = rank_list[:]
        provisory_suits = suits_list[:]

        # findout the suit
        for i in Counter(provisory_suits).items():
            if i[1] < 5:

                #remove all the elements
                while i[0] in provisory_suits:
                    pos = provisory_suits.index(i[0])
                    provisory_suits.remove(i[0])
                    provisory_ranks.remove(provisory_ranks[pos])

        # after remove the rank with different suits, time to verify the sequence
        list = sorted(provisory_ranks)
        test = [list[i:i + 5] for i in range(0, len(list) - 4) if list[i] == list[i + 4] - 4]
        if len(test)>0:
            return True
        else:
            return False
    else:
        return False


def fullhouse(rank_list):
    if pair(rank_list) and three_kind(rank_list):
        return True
    else:
        return False

def straight(rank_list):
    list = sorted(set(rank_list[:]))
    test = [list[i:i+5] for i in range(0,len(list)-4) if list[i] == list[i+4]-4]
    if len(test) > 0:
        return True
    else:
        return False

def flush(suits_list):
    if {5, 6, 7} & set(Counter(suits_list).values()):
        return True
    else:
        return False

def three_kind(rank_list):
    if 3 in Counter(rank_list).values():
        return True
    else:
        return False

def two_pairs(rank_list):
    if list(Counter(rank_list).values()).count(2) >= 2:
        return True
    else:
        return False

def pair(rank_list):
    if list(Counter(rank_list).values()).count(2) == 1:
        return True
    else:
        return False

def statistic(rank_list, suit_list):
    dict = {}

    return dict