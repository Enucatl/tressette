#coding=utf-8

import carta
import random

def trova_battuta(carte_giocate):
    num_battuta = 0
    for battuta in carte_giocate:
        for c in battuta:
            #try:
            #    c + 1
            #except TypeError:
            #    return num_battuta
            if not isinstance(c, carta.Carta):
                return num_battuta
        num_battuta += 1
    return -1

class Giocatore(object):

    def __init__(self, carte_in_mano, squadra):
        #per carte_in_mano si intende una lista di oggetti Carta
        self.carte_in_mano = sorted(carte_in_mano, carta.ordine_convenzionale)
        self.squadra = squadra
        self.carte_in_mano

    def gioca_carta(self, carte_giocate=0):
        num_battuta_in_corso = trova_battuta(carte_giocate)
        battuta_in_corso = carte_giocate[num_battuta_in_corso]
        battuta_in_corso = enumerate(battuta_in_corso)
        battuta_in_corso = [c for c in battuta_in_corso if isinstance(c[1],
            carta.Carta)]

        giocate_legali = []
        if not battuta_in_corso:
            #se la battuta è vuota, significa che è primo di mano, quindi
            #può giocare come preferisce
            giocate_legali = self.carte_in_mano
        else:
            comanda = 0
            for i in range(4):
                comanda = battuta_in_corso[i][1]
                if (battuta_in_corso[i - 1][0] % 4 != battuta_in_corso[i][0]
                    % 4 or len(battuta_in_corso) == 1):
                        break
            giocate_legali = [c for c in self.carte_in_mano
                if carta.stesso_palo(c, comanda)]
            #filtra la lista delle carte che ha in mano, essendo costretto a
            #rispondere al palo
            if not giocate_legali:
            #se non può rispondere al palo, può giocare come vuole
                giocate_legali = self.carte_in_mano
        giocata = random.choice(giocate_legali)

        del self.carte_in_mano[self.carte_in_mano.index(giocata)]
        return giocata
        
