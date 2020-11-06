import pandas as pd
import random

deck = ['2-h','3-h','4-h','5-h','6-h','7-h','8-h','9-h','10-h','J-h','Q-h','K-h','A-h','2-d','3-d','4-d','5-d','6-d','7-d','8-d','9-d','10-d','J-d','Q-d','K-d','A-d','2-c','3-c','4-c','5-c','6-c','7-c','8-c','9-c','10-c','J-c','Q-c','K-c','A-c','2-s','3-s','4-s','5-s','6-s','7-s','8-s','9-s','10-s','J-s','Q-s','K-s','A-s']

def premier_tirage(deck):
    tirage = random.sample(deck, 5)
    for i in tirage:
        deck.remove(i)
    return tirage, deck


def choix_carte(chosen_cards):
    jeu = []
    compteur = 0
    for card in chosen_cards:
        if compteur < 4:
            answer = input(f'Voulez vous garder la carte {card} (y/n)? : ')
            if answer == 'y':
                compteur += 1
                jeu.append(card)
            else:
                continue
    return jeu


def deuxieme_tirage(jeu, deck):
    nb_carte = len(jeu)
    cartes_a_tirer = 5 - nb_carte
    nouvelle_carte = random.sample(deck, cartes_a_tirer)
    for i in nouvelle_carte:
        jeu.append(i)
    return jeu



def machine():
    tirage, restant_deck = premier_tirage(deck)
    print("Tirage : ")
    print(tirage)
    jeu_choisi = choix_carte(tirage)
    jeu_final = deuxieme_tirage(jeu_choisi, restant_deck)
    print("Tirage final : ")
    print(jeu_final)

machine()

def decompose_jeu(tirage):
    dic = {}
    keys = [1,2,3,4,5]
    valeur = []
    couleur = []
    for i,k in zip(tirage, keys):
        dic[k] = i.split('-')
    for key in dic.keys():
        valeur.append(dic[key][0])
        couleur.append(dic[key][1])
    return valeur, couleur

def convert_carte(liste):
    for e,i in zip (liste, range(0,5)):
        try:
            liste[i] = int(e)
        except:
            if e == 'J':
                liste[i] = 11
            elif e == 'Q':
                liste[i] = 12
            elif e == 'K':
                liste[i] = 13
            elif e == 'A':
                liste[i] = 1
            else:
                continue
    return liste

def quinte_flush(tirage):
    valeur, couleur = decompose_jeu(tirage)
    valeur = convert_carte(valeur)
    valeur = sorted(valeur)
    suite = []
    for e,i in zip(valeur[0:-1], range(len(valeur)-1)):
        if e+1 == valeur[i+1]:
            suite.append('True')
    if suite.count('True') == 4 and couleur.count(couleur[0]) == 5:
        return True
    else:
        return False

def quinte_flush_royale(tirage):
    valeur_gagnante = ['10', 'J', 'Q', 'K', 'A']
    valeur, couleur = decompose_jeu(tirage)
    if sorted(valeur_gagnante) == sorted(valeur) and couleur.count(couleur[0]) == 5:
        return True
    else:
        return False

def carre(tirage):
    valeur, couleur = decompose_jeu(tirage)
    valeur1 = pd.Series(valeur)
    uniques = valeur1.unique()
    count = []
    for i in uniques:
        count.append(valeur.count(i))
    if len(uniques) == 2 and sorted(count) == [1, 4]:
        return True
    else:
        return False

def full(tirage):
    valeur, couleur = decompose_jeu(tirage)
    valeur1 = pd.Series(valeur)
    uniques = valeur1.unique()
    count = []
    for i in uniques:
        count.append(valeur.count(i))
    if len(uniques) == 2 and sorted(count) == [2, 3]:
        return True
    else:
        return False

def flush(tirage):
    valeur, couleur = decompose_jeu(tirage)
    if couleur.count(couleur[0]) == 5:
        return True
    else:
        return False




# test_nunique =  nunique(carte)
# couleur = ["s","s","x","x","s"]
# carte = ["d","d","k","k","k"]
#
# def nunique(couleur):
#     nb_couleur = []
#     for x in set(couleur):
#         nb_couleur.append(couleur.count(x))
#     return(sorted(nb_couleur,reverse=True))[:2]
#
# def quinte_flush_royal(carte, couleur):
#     return sorted(carte) == sorted(['10','J','Q','K','A']) and couleur.count(couleur[0])==5
#
#
# if test_nunique[0]==4:
#     print("carre")
# elif test_nunique[0]==3 and test_nunique[1]==2 :
#     print("full")
# elif test_nunique[0]==3:
#     print("brelan")
# elif test_nunique[0]==2 and test_nunique[1]==2 :
#     print("double pairs")
#
#
# def check_suite(carte):
#     for x in carte[:-1]:
#         if sorted(carte) == sorted([1, 10, 11, 12, 13]):
#             return True
#         elif x+1 == carte[x]:
#             return True
#             print(x)
#         else:
#             return False
#
#
# couleur_nunique =  nunique(couleur)
# carte_nunique =  nunique(couleur)
