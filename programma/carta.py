#coding=utf-8

def ordine_convenzionale(x, y):
    if x.palo > y.palo:
        return 1
    elif x.palo == y.palo:
        if x > y:
            return 1
        else: return -1
    else: return -1

def stesso_palo(x, y):
    if x.palo == y.palo:
        return True
    else:
        return False

def comanda_battuta(battuta, primo_di_mano):
    """prende la lista delle carte della battuta, vede chi è primo di mano e
    decide chi prende. Restituisce l'indice di chi ha conquistato la
    battuta"""
    comanda = battuta[primo_di_mano]
    """ordina le carte nell'ordine in cui sono state giocate per un'iterazione più comoda:"""
    battuta_ordinata = battuta[primo_di_mano:] + battuta[:primo_di_mano]
    """cerca la meglio"""
    for risposta in battuta_ordinata:
        if not comanda > risposta:
            comanda = risposta
    return battuta.index(comanda)

class Carta(object):

    def __init__(self, numero):
        self.palo = numero // 10
        self.valore = (numero % 10) + 1
        #così i valori sono da 1 a 10 e non 0-9
        valgono_uno = [2, 3, 8, 9, 10]
        valgono_tre = [1]
        if self.valore in valgono_uno:
            self.punti = 1
        elif self.valore in valgono_tre:
            self.punti = 3
        else: self.punti = 0

    def __repr__(self):
        diz_pali = {3:'denari', 2:'spade', 1:'coppe', 0:'bastoni'}
        diz_valori = {1:'Asso', 2:'Due', 3:'Tre', 4:'Quattro',
                5:'Cinque', 6: 'Sei', 7: 'Sette', 8: 'Fante',
                9: 'Cavallo', 10: 'Re'}
        return diz_valori[self.valore] + ' di ' + diz_pali[self.palo]

    def __gt__(self, other):
        potenza = [4, 5, 6, 7, 8, 9, 10, 1, 2, 3]
        if other.palo != self.palo:
            return True
        elif potenza.index(self.valore) > potenza.index(other.valore):
            return True
        else:
            return False

    def __eq__(self, other):
        if other.palo == self.palo and self.valore == other.valore:
            return True
        else: return False

    def __ne__(self, other):
        if other.palo != self.palo or self.valore != other.valore:
            return True
        else: return False

    #def __lt__(self, other):
    #    potenza = [4, 5, 6, 7, 8, 9, 10, 1, 2, 3]
    #    if other.palo != self.palo:
    #        return True
    #    elif potenza.index(self.valore) < potenza.index(other.valore):
    #        return True
    #    else:
    #        return False
