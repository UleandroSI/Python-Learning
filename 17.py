# Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não
# bissexto.

# Entrada
ano = int(input("Digite o ano: "))

# Execuçao
if ano % 400 == 0:
    print("Ano bissexto.")
else:
    if ano % 4 == 0 and ano % 100 != 0:
        print("Ano bissexto.")
    else:
        print("Ano não bissexto.")