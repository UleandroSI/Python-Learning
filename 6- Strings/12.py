#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 24 18:39:58 2020

@author: leandro
"""
# Valida e corrige número de telefone'''. Faça um programa que leia um 
# número de telefone, e corrija o número no caso deste conter somente 7 
# dígitos, acrescentando o '3' na frente. O usuário pode informar o número 
# com ou sem o traço separador.
# Valida e corrige número de telefone
# Telefone: 461-0133
# Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.
# Telefone corrigido sem formatação: 34610133
# Telefone corrigido com formatação: 3461-0133

# Declaracoes
def limpar (telefone):
    num = ['0','1','2','3','4','5','6','7','8','9']
    x = 0
    numeros_limpo = []
    while x < len(telefone):
        if telefone[x] in num:
            numeros_limpo.append(str(telefone[x]))
        x += 1
    return(numeros_limpo)
y=0
fone = ''
telefone = input("Digite o numero do telefone: ")
numeros= limpar(telefone)
if len(numeros ) < 7:
    print("Telefone inválido.")
elif len(numeros ) == 7:
    print("Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.")
    numeros.insert(0,'3')
numeros = ''.join(numeros)
fone = int(numeros)
print("Telefone: ",fone)