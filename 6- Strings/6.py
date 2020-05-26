#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 24 18:39:58 2020

@author: leandro
"""
# Data por extenso. Faça um programa que solicite a data de nascimento 
#(dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso.
# Data de Nascimento: 29/10/1973
# Você nasceu em  29 de Outubro de 1973.

# VARIAVEIS
def validar(data):
    mes_extenso = ''
    from datetime import date
    data_atual = date.today()
    ano_atual = int('{}'.format(data_atual.year))
    #print(ano_atual) Teste do ano atual
    #VALIDANDO DATA
    if len(data) != 10:
        return 'ERRO DE FORMATO'
    elif data[2] != '/' or data[5] != '/':
        return 'ERRO DE FORMATO'
    elif data[6] not in('1234567890'):
        return 'ERRO DE FORMATO'
    elif data[7] not in('1234567890'):
        return 'ERRO DE FORMATO'
    elif data[8] not in('1234567890'):
        return 'ERRO DE FORMATO'
    elif data[9] not in('1234567890'):
        return 'ERRO DE FORMATO'
    else:
        dia = int(data[0:2])
        mes = int(data[3:5])
        ano = int(data[6:])
        if ano < 0 or ano > ano_atual:
            return 'ERRO DE FORMATO'
        else:
            if dia < 0 or dia > 31:
                return 'ERRO DE FORMATO'
            else:
                if mes < 0 or mes > 12:
                    return 'ERRO DE FORMATO'
                else:
                    if mes == 1:
                        mes_extenso = 'janeiro'
                    elif mes == 2:
                        mes_extenso = 'fevereiro'
                        if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0:
                            if dia > 29:
                                return 'ERRO DE FORMATO'
                        else:
                            if dia > 28:
                                return 'ERRO DE FORMATO'
                    elif mes == 3:
                        mes_extenso = 'março'
                    elif mes == 4:
                        mes_extenso = 'abril'
                        if dia > 30:
                            return 'ERRO DE FORMATO'
                    elif mes == 5:
                        mes_extenso = 'maio'
                    elif mes == 6:
                        mes_extenso = 'junho'
                        if dia > 30:
                            return 'ERRO DE FORMATO'
                    elif mes == 7:
                        mes_extenso = 'julho'
                    elif mes == 8:
                        mes_extenso = 'agosto'
                    elif mes == 9:
                        mes_extenso = 'setembro'
                        if dia > 30:
                            return 'ERRO DE FORMATO'
                    elif mes == 10:
                        mes_extenso = 'outubro'
                    elif mes == 11:
                        mes_extenso = 'novembro'
                        if dia > 30:
                            return 'ERRO DE FORMATO'
                    else:
                        mes_extenso = 'dezembro'
               
        print("Você nasceu em %d de %s de %d." %(dia, mes_extenso, ano))

# PROCESSAMENTO
data = input("Digite a data no formato 'DD/MM/AAAA': ")
valido = validar(data)
if valido == 'ERRO DE FORMATO':
    print(valido)