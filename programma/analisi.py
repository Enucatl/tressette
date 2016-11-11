#!/usr/bin/env python
#coding=utf-8

from __future__ import division, print_function

from ROOT import TH1F

input = open('punteggi')

hist = TH1F("punteggi", "punteggi", 11, 0, 11)
for line in input:
    hist.Fill(float(line))

hist.Draw()
raw_input()
