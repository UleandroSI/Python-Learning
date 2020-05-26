# '''Data com mês por extenso'''. Construa uma função que receba uma data 
# no formato ''DD/MM/AAAA'' e devolva uma string no formato 
# ''D de mesPorExtenso de AAAA''. Opcionalmente, valide a data e retorne 
# NULL caso a data seja inválida.

# VARIAVEIS
def validar(data):
    mes_extenso = ''
    from datetime import date
    data_atual = date.today()
    ano_atual = int('{}'.format(data_atual.year))
    #print(ano_atual) Teste do ano atual
    #VALIDANDO DATA
    if len(data) != 10:
        return 'NULL'
    elif data[2] != '/' or data[5] != '/':
        return 'NULL'
    elif data[6] not in('1234567890'):
        return 'NULL'
    elif data[7] not in('1234567890'):
        return 'NULL'
    elif data[8] not in('1234567890'):
        return 'NULL'
    elif data[9] not in('1234567890'):
        return 'NULL'
    else:
        dia = int(data[0:2])
        mes = int(data[3:5])
        ano = int(data[6:])
        if ano < 0 or ano > ano_atual:
            return 'NULL'
        else:
            if dia < 0 or dia > 31:
                return 'NULL'
            else:
                if mes < 0 or mes > 12:
                    return 'NULL'
                else:
                    if mes == 1:
                        mes_extenso = 'janeiro'
                    elif mes == 2:
                        mes_extenso = 'fevereiro'
                        if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0:
                            if dia > 29:
                                return 'NULL'
                        else:
                            if dia > 28:
                                return 'NULL'
                    elif mes == 3:
                        mes_extenso = 'março'
                    elif mes == 4:
                        mes_extenso = 'abril'
                        if dia > 30:
                            return 'NULL'
                    elif mes == 5:
                        mes_extenso = 'maio'
                    elif mes == 6:
                        mes_extenso = 'junho'
                        if dia > 30:
                            return 'NULL'
                    elif mes == 7:
                        mes_extenso = 'julho'
                    elif mes == 8:
                        mes_extenso = 'agosto'
                    elif mes == 9:
                        mes_extenso = 'setembro'
                        if dia > 30:
                            return 'NULL'
                    elif mes == 10:
                        mes_extenso = 'outubro'
                    elif mes == 11:
                        mes_extenso = 'novembro'
                        if dia > 30:
                            return 'NULL'
                    else:
                        mes_extenso = 'dezembro'
        print("%d de %s de %d" %(dia, mes_extenso, ano))

# PROCESSAMENTO
data = input("Digite a data no formato 'DD/MM/AAAA': ")
valido = validar(data)
if valido == 'NULL':
    print(valido)