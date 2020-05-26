#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 24 18:39:58 2020

@author: leandro
"""
# 1. '''Tamanho de strings.''' Faça um programa que leia 2 strings e informe 
# o conteúdo delas seguido do seu comprimento. Informe também se as duas 
# strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.
#Compara duas strings
#String 1: Brasil Hexa 2006
#String 2: Brasil! Hexa 2006!
#Tamanho de "Brasil Hexa 2006": 16 caracteres
#Tamanho de "Brasil! Hexa 2006!": 18 caracteres
#As duas strings são de tamanhos diferentes.
#As duas strings possuem conteúdo diferente.

# VARIAVEIS
def compara(texto1, texto2):
    tamanho1 = int(len(texto1))
    tamanho2 = int(len(texto2))
    if texto1 == texto2:
        print("As duas strings são de tamanhos iguais.")
    else:
        print("Tamanho de ' %s ': %d caracteres" %(texto1, tamanho1))
        print("Tamanho de ' %s ': %d caracteres" %(texto2, tamanho2))
        print("As duas strings são de tamanhos diferentes.")
        print("As duas strings possuem conteúdo diferente.")

texto1 = input("Digite a primeira String: ")
texto2 = input("Digite a segunda String: ")

# PROCESSAMENTO
compara(texto1, texto2)