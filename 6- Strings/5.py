#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 24 18:39:58 2020

@author: leandro
"""
# Nome na vertical em escada invertida. Altere o programa anterior de modo 
# que a escada seja invertida.
#FULANO
#FULAN
#FULA
#FUL
#FU
#F

# VARIAVEIS
nome = input("Digite seu nome: ")
#PROCESSAMENTO
nome = nome.upper()
for x in range(len(nome),-1,-1):
    print(nome[:x])