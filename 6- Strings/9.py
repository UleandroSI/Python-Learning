#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 24 18:39:58 2020

@author: leandro
"""
# Verificação de CPF.''' Desenvolva um programa que solicite a digitação de um 
# número de CPF no formato '''xxx.xxx.xxx-xx''' e indique se é um número válido 
# ou inválido através da validação dos dígitos verificadores edos caracteres de 
# formatação.

# VARIAVEIS
def valida_estrutura(cpf):
    if cpf[3] != '.' or cpf[7] != '.' or cpf[11] != '-':
        print("CPF invalido.")
        return False
    else:
        global separado
        separado = cpf.split('.')
        primeiro = int(separado[0])
        segundo = int(separado[1])
        traco = separado[2]
        traco = traco.split('-')
        terceiro = int(traco[0])
        quarto = int(traco[1])
        #print(separado)
        print(primeiro)
        print(segundo)
        print(terceiro)
        #print(traco)
        print(quarto)
        return True

def calcular_p_digito(cpf):
    trio1 = (int(cpf[0]) * 10)+(int(cpf[1]) * 9)+(int(cpf[2]) * 8)
    trio2 = (int(cpf[4]) * 7)+(int(cpf[5]) * 6)+(int(cpf[6]) * 5)
    trio3 = (int(cpf[8]) * 4)+(int(cpf[9]) * 3)+(int(cpf[10]) * 2)
    soma1 = trio1 + trio2 + trio3
    resto1 = soma1 % 11
    if resto1 < 2:
        digito1 = 0
    else:
        digito1 = 11 - resto1
    
    if digito1 != int(cpf[12]):
        return False
    else:
        return True
        
def calcular_s_digito(cpf):
    soma2 = (int(cpf[0]) * 11)+(int(cpf[1]) * 10)+(int(cpf[2]) * 9)+(int(cpf[4]) * 8)+(int(cpf[5]) * 7)+(int(cpf[6]) * 6)+(int(cpf[8]) * 5)+(int(cpf[9]) * 4)+(int(cpf[10]) * 3)+(int(cpf[12]) * 2)
    resto2 = soma2 % 11
    if resto2 < 2:
        digito2 = 0
    else:
        digito2 = 11 - resto2
    
    if digito2 != int(cpf[13]):
        return False
    else:
        return True
    
cpf = input("Digite o CPF no formato xxx.xxx.xxx-xx: ")

# PROCESSAMENTO
estrutura = valida_estrutura(cpf)
if estrutura:
    pri_digito = calcular_p_digito(cpf)
    if pri_digito:
        seg_digito = calcular_s_digito(cpf)
        if seg_digito:
            print("CPF valido.")
        else:
            print("CPF invalido.")
    else:
        print("CPF invalido.")
else:
    print("CPF invalido.")