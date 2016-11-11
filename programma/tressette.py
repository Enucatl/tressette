#!/usr/bin/env python
#coding=utf-8

from __future__ import division, print_function
import carta
import passata
import random
import giocatore

mazzo = range(40)
random.shuffle(mazzo)
mazzo = [carta.Carta(x) for x in mazzo]

giocatori = [giocatore.Giocatore(mazzo[0:10], 1),
        giocatore.Giocatore(mazzo[10:20], 2),
        giocatore.Giocatore(mazzo[20:30], 1),
        giocatore.Giocatore(mazzo[30:40], 2)]

cartaro = 3
primo_di_mano= (cartaro + 1) % 4
passata = passata.Passata(giocatori, primo_di_mano)
for i in range(10):
    passata.battuta()
passata.punteggi()
