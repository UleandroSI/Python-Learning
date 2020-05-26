#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 24 18:39:58 2020

@author: leandro
"""
# Nome na vertical em escada. Modifique o programa anterior de forma a 
# mostrar o nome em formato de escada.
#F
#FU
#FUL
#FULA
#FULAN
#FULANO

# VARIAVEIS
nome = input("Digite seu nome: ")
#PROCESSAMENTO
nome = nome.upper()
for x in range(0, len(nome)+1):
    print(nome[:x])