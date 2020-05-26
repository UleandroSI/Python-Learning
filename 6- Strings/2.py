#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 24 18:39:58 2020

@author: leandro
"""
# Nome ao contrário em maiúsculas.''' Faça um programa que permita ao usuário 
# digitar o seu nome e em seguida mostre o nome do usuário de trás para 
# frente utilizando somente letras maiúsculas. Dica: lembre−se que ao informar 
# o nome o usuário pode digitar letras maiúsculas ou minúsculas.

# VARIAVEIS
nome = input("Digite seu nome: ")

# PROCESSAMENTO
nome = nome.upper()
print(nome[::-1])