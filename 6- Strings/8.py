#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 24 18:39:58 2020

@author: leandro
"""
# Palíndromo.''' Um palíndromo é uma seqüência de caracteres cuja leitura é 
# idêntica se feita da direita para esquerda ou vice−versa. Por exemplo: 
# '''OSSO''' e '''OVO''' são palíndromos. Em textos mais complexos os espaços 
# e pontuação são ignorados. A frase '''SUBI NO ONIBUS''' é o exemplo de uma 
# frase palíndroma onde os espaços foram ignorados. Faça um programa que leia 
# uma seqüência de caracteres, mostre−a e  diga se é um palíndromo ou não.

#VARIAVEIS
inversa = ''
palavra = input("Digite a palavra: ")
# PROCESSAMENTO
junta = palavra.replace(" ", "")
inversa = junta[::-1]
if junta == inversa:
    print(palavra, "- Palavra Palindroma")
else:
    print(palavra, "- Palavra não Palindroma")