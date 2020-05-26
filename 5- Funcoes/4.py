# Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’,
# se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.

def argumento(x):
    if x > 0:
        print("Argumento P")
    else:
        print("Argumento N")
#VARIAVEIS
x = int(input("Digite um numero: "))
argumento(x)