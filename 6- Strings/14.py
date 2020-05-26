#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 24 21:44:05 2020

@author: leandro
"""

#Leet spek generator. Leet é uma forma de se escrever o alfabeto latino 
#usando outros símbolos em lugar das letras, como números por exemplo. 
#A própria palavra leet admite muitas variações, como l33t ou 1337. 
#O uso do leet reflete uma subcultura relacionada ao mundo dos jogos de 
#computador e internet, sendo muito usada para confundir os iniciantes e 
#afirmar-se como parte de um grupo.  Pesquise sobre as principais formas de 
#traduzir as letras. Depois, faça um programa que peça uma texto e 
#transforme-o para a grafia leet speak.

def transforma(texto):
    betoalfa = {' ':' ','.':'.','!':'!','a':'@','b':'6','c':'(','d':'&','e':'3'}
    conversao = ''
    for x in texto:
        conversao = conversao + betoalfa[x]
    return conversao
texto = input('Digite o texto: ')
traduzido = transforma(texto)
print(traduzido)
#print(betoalfa.keys())