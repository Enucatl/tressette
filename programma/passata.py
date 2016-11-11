#coding=utf-8

from __future__ import division, print_function
import carta

class Passata(object):

    def __init__(self, giocatori, primo_di_mano):
        self.giocatori = giocatori
#i giocatori devono cominciare in ordine nella lista:
        self.primo_di_mano = primo_di_mano
        self.carte_giocate = [[0 for _ in range(4)] for _ in range(10)]
#conta le battute:
        self.battuta_in_corso = 0
#ricorda chi ha conquistato le battute precedenti
        self.vincitori_battute = []

    def battuta(self):
        """gioca il primo di mano, poi gli altri tre a seguire, ricevendo come
        informazione tutte le carte uscite fino a quel momento.
        le carte giocate vengono salvate in self.carte_giocate a mano a mano
        che escono, per facilitare l'implementazione di
        Giocatore.gioca_carta()"""

#crea un elemento della lista che conterrà le carte della battuta
#aggiunge la giocata del primo giocatore
        battuta_in_corso = self.battuta_in_corso
        comanda = self.giocatori[self.primo_di_mano].gioca_carta(self.carte_giocate)
        self.carte_giocate[battuta_in_corso][self.primo_di_mano] = comanda
        for i in range(1, 4):
            num_giocatore = (self.primo_di_mano + i) % 4
            risposta = self.giocatori[num_giocatore].gioca_carta(self.carte_giocate)
            self.carte_giocate[battuta_in_corso][num_giocatore] = risposta
        """controlla chi ha preso la battuta"""
        battuta_completa = self.carte_giocate[battuta_in_corso]
        piglia = carta.comanda_battuta(battuta_completa, self.primo_di_mano)
        comanda = battuta_completa[piglia]
        self.battuta_in_corso += 1
        self.vincitori_battute.append(piglia)
        print(battuta_completa)
        print('comanda il', comanda)
#chi ha preso comincia la battuta seguente
        self.primo_di_mano = piglia
        print('prende il giocatore', piglia + 1, '\n')

    def punteggi(self):
        """Calcola i punti dei giocatori e quindi delle squadre"""
        punteggi_giocatori = [0 for giocatore in self.giocatori]
        for battuta, vincitore in zip(self.carte_giocate, self.vincitori_battute):
            punti_battuta = sum([c.punti for c in battuta])
            punteggi_giocatori[vincitore] += punti_battuta
        squadre = set([giocatore.squadra for giocatore in self.giocatori])
        punteggi_squadre = [(squadra, 0) for squadra in squadre]
        punteggi_squadre = dict(punteggi_squadre)
        for giocatore, punteggio in zip(self.giocatori, punteggi_giocatori):
            punteggi_squadre[giocatore.squadra] += punteggio
        for squadra in punteggi_squadre:
            punteggi_squadre[squadra] = punteggi_squadre[squadra] // 3
        squadra_tola = self.giocatori[self.vincitori_battute[-1]].squadra
        punteggi_squadre[squadra_tola] += 1
        print(punteggi_squadre[1])


        
