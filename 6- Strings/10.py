#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 24 18:39:58 2020

@author: leandro
"""
# Número por extenso.''' Escreva um programa que solicite ao usuário a 
# digitação de um número até 99 e imprima-o na tela por extenso.

dicionario = {}
dicionario['0'] = 'zero'
dicionario['1'] = 'um'
dicionario['2'] = 'dois'
dicionario['3'] = 'três'
dicionario['4'] = 'quatro'
dicionario['5'] = 'cinco'
dicionario['6'] = 'seis'
dicionario['7'] = 'sete'
dicionario['8'] = 'oito'
dicionario['9'] = 'nove'
dicionario['10'] = 'dez'
dicionario['11'] = 'onze'
dicionario['12'] = 'doze'
dicionario['13'] = 'treze'
dicionario['14'] = 'quatorze'
dicionario['15'] = 'quinze'
dicionario['16'] = 'dezesseis'
dicionario['17'] = 'dezessete'
dicionario['18'] = 'dezoito'
dicionario['19'] = 'dezenove'
dicionario['20'] = 'vinte'
dicionario['30'] = 'trinta'
dicionario['40'] = 'quarenta'
dicionario['50'] = 'cinquenta'
dicionario['60'] = 'sessenta'
dicionario['70'] = 'setenta'
dicionario['80'] = 'oitenta'
dicionario['90'] = 'noventa'

while True:
    numero = int(input("Digite um numero de '0 a 99': "))
    if numero < 0 or numero > 99:
        print("Digite o numero novamente.")
    else:
        break

numero = str(numero)
if len(numero) < 2:
    if numero == '0':
        print('Numero: ',dicionario['0'])
    elif numero == '1':
        print('Numero: ',dicionario['1'])
    elif numero == '2':
        print('Numero: ',dicionario['2'])
    elif numero == '3':
        print('Numero: ',dicionario['3'])
    elif numero == '4':
        print('Numero: ',dicionario['4'])
    elif numero == '5':
        print('Numero: ',dicionario['5'])
    elif numero == '6':
        print('Numero: ',dicionario['6'])
    elif numero == '7':
        print('Numero: ',dicionario['7'])
    elif numero == '8':
        print('Numero: ',dicionario['8'])
    else:
        print('Numero: ',dicionario['9'])
else:
    if numero == '10':
        print('Numero: ',dicionario['10'])
    elif numero == '11':
        print('Numero: ',dicionario['11'])
    elif numero == '12':
        print('Numero: ',dicionario['12'])
    elif numero == '13':
        print('Numero: ',dicionario['13'])
    elif numero == '14':
        print('Numero: ',dicionario['14'])
    elif numero == '15':
        print('Numero: ',dicionario['15'])
    elif numero == '16':
        print('Numero: ',dicionario['16'])
    elif numero == '17':
        print('Numero: ',dicionario['17'])
    elif numero == '18':
        print('Numero: ',dicionario['18'])
    elif numero == '19':
        print('Numero: ',dicionario['19'])
    elif numero == '20':
        print('Numero: ',dicionario['20'])
        
    elif numero[0] == '2':
        print('Numero: ',dicionario['20'], 'e', dicionario[numero[1]] )
    elif numero[0] == '3':
        print('Numero: ',dicionario['30'], 'e', dicionario[numero[1]] )
    elif numero[0] == '4':
        print('Numero: ',dicionario['40'], 'e', dicionario[numero[1]] )
    elif numero[0] == '5':
        print('Numero: ',dicionario['50'], 'e', dicionario[numero[1]] )
    elif numero[0] == '6':
        print('Numero: ',dicionario['60'], 'e', dicionario[numero[1]] )
    elif numero[0] == '7':
        print('Numero: ',dicionario['70'], 'e', dicionario[numero[1]] )
    elif numero[0] == '8':
        print('Numero: ',dicionario['80'], 'e', dicionario[numero[1]] )
    elif numero[0] == '9':
        print('Numero: ',dicionario['90'], 'e', dicionario[numero[1]] )