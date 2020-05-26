#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 25 12:16:13 2020

@author: leandro
"""

#Faça um programa que leia um arquivo texto contendo uma lista de endereços 
#IP e gere um outro arquivo, contendo um relatório dos endereços IP válidos e inválidos.
#        O arquivo de entrada possui o seguinte formato: 
#    200.135.80.9
#    192.168.1.1
#    8.35.67.74
#    257.32.4.5
#    85.345.1.2
#    1.2.3.4
#    9.8.234.5
#    192.168.0.256
#        O arquivo de saída possui o seguinte formato: 
#    [Endereços válidos:]
#    200.135.80.9
#    192.168.1.1
#    8.35.67.74
#    1.2.3.4
#    [Endereços inválidos:]
#    257.32.4.5
#    85.345.1.2
#    9.8.234.5
#    192.168.0.256