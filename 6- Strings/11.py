#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 24 18:39:58 2020

@author: leandro
"""
# Jogo de Forca.''' Desenvolva um jogo da forca. 
# O programa terá uma lista de palavras  lidas de um arquivo texto 
# e escolherá uma aleatoriamente. O jogador poderá errar 6 vezes antes 
# de ser enforcado.
# Digite uma letra: A
# -> Você errou pela 1ª vez. Tente de novo!
# Digite uma letra: O
# A palavra é: _ _ _ _ O
# Digite uma letra: E
# A palavra é: _ E _ _ O
# Digite uma letra: S
# -> Você errou pela 2ª vez. Tente de novo!

# Variaveis
acertos = erros = 0
# PRocessamento
print("JOGO DA FORCA!")
with open('palavras.txt', 'r') as x:
    letras = len(x)
    choice palavra no arquivo
    print substituindo as letras
    receber letra