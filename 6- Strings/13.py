#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 24 18:39:58 2020

@author: leandro
"""
#Jogo da palavra embaralhada. Desenvolva um jogo em que o usuário tenha que 
#adivinhar uma palavra que será mostrada com as letras embaralhadas. 
#O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma 
#aleatoriamente. O jogador terá seis tentativas para adivinhar a palavra. 
#Ao final a palavra deve ser mostrada na tela, informando se o usuário ganhou 
#ou perdeu o jogo.
import random
erros = 0
def embaralha (palavra):
    mist = list(palavra)
    random.shuffle(mist)
    return ''.join(mist)

print('=== Jogo da palavra embaralhada==='.center(5))
print('--Você tem 6 chances para acertar a palavra--'.center(5))
palavra = random.choice(open('13.txt').readlines())
palavra = palavra.rstrip()
lista = embaralha(palavra)
print('A palavra da vez é: ',lista)
while erros < 6:
    resposta = input('Digite sua resposta: ')
    if resposta != palavra:
        erros += 1
        print('palavra errada')
        if erros == 6:
            print('Você perdeu!')
            print('%s'.center(15) %(palavra))
    else:
        erros = 6
        print('Você acertou!')
        print('%s'.center(15) %(palavra))