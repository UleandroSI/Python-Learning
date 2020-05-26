# Faça um Programa que peça um número correspondente a um determinado 
#ano e em seguida informe se este ano é ou não bissexto.

#VARIAVEIS
ano = int(input("Digite o ano: "))
#PROCESSAMENTO
if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0:
    print("Ano bissexto.")
else:
    print("Ano não bissexto.")