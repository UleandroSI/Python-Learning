# Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

def soma(a,b,c):
    total = a+b+c
    return total
#VARIAVEIS
a = int(input("Digite o primeiro numero: "))
b = int(input("Digite o segundo numero: "))
c = int(input("Digite o terceiro numero: "))
print("Soma dos numeros: %d" %soma(a,b,c))