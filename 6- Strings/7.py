#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 24 18:39:58 2020

@author: leandro
"""
# Conta espaços e vogais.''' Dado uma string com uma frase informada pelo usuário 
# (incluindo espaços em branco), conte:
#  a. quantos espaços em branco existem na frase.
#  a. quantas vezes aparecem as vogais a, e, i, o, u.

# VARIAVEIS
frase = input("Digite a frase: ")
cont_espace = cont_vogal = 0
vogais = 'a,e,i,o,u'

# PROCESSAMENTO
for x in frase:
    if x == ' ':
        cont_espace += 1
    if x in vogais:
        cont_vogal += 1
        
print(" Existem %d espaços em branco." %cont_espace)
print(" Existem %d vogais" %cont_vogal)