#Faça um programa que leia um arquivo texto contendo uma lista
# de endereços IP e gere um outro arquivo, contendo um relatório
# dos endereços IP válidos e inválidos.
#    O arquivo de entrada possui o seguinte formato:

#200.135.80.9
#192.168.1.1
#8.35.67.74
#257.32.4.5
#85.345.1.2
#1.2.3.4
#9.8.234.5
#192.168.0.256
#    O arquivo de saída possui o seguinte formato:
#[Endereços válidos:]
#200.135.80.9
#192.168.1.1
#8.35.67.74
#1.2.3.4
#[Endereços inválidos:]
#257.32.4.5
#85.345.1.2
#9.8.234.5
#192.168.0.256

#VARIAVEIS
'''def validarIP(linha):
    separar = linha.rstrip().split('.') # rstrip:remove caracter de quebra de linha split('.'):separa conteudo pelo .
    primeiro = int(separar[0])
    segundo = int(separar[1])
    terceiro = int(separar[2])
    quarto = int(separar[3])
    if primeiro <= 0 or primeiro >= 256:
        print("Invalido")
    else:
        if '''
'''
def gera_arquivo(validos,invalidos):
    pass
'''

arquivo = open('enderecos.txt', 'r')
validos, invalidos = [], []
# PROCESSAMENTO
for linha in arquivo.readlines():
    #retorno = validarIP(linha)
    separar = linha.rstrip().split('.')  # rstrip:remove caracter de quebra de linha split('.'):separa conteudo pelo .
    primeiro = int(separar[0])
    segundo = int(separar[1])
    terceiro = int(separar[2])
    quarto = int(separar[3])
    if primeiro <= 0 or primeiro >= 255:
        invalidos.append(linha)
    else:
        if segundo <= 0 or segundo >= 255:
            invalidos.append(linha)
        else:
            if terceiro <= 0 or terceiro >= 255:
                invalidos.append(linha)
            else:
                if quarto <= 0 or quarto >= 255:
                    invalidos.append(linha)
                else:
                    validos.append(''.join(linha))
# SAIDA
print("Validos: ")
print(validos)
print("Invalidos: ")
print(invalidos)
arquivo.close()
ip = open('IPs.txt', 'w')
ip.write("Endereços válidos:\n")
for x in range(0, len(validos)):
    ip.write(validos[x])
ip.write("\n")
ip.write("Endereços inválidos:\n")
for y in range(0, len(invalidos)):
    ip.write(invalidos[y])