# Encontrar numeros primos e uma tarefa dificil. Faça um programa que gera uma
#lista dos numeros primos existentes entre 1 e um numero inteiro informado.

i = 1
primos = []
numero = int(input('Digite um número inteiro: '))

while i <= numero:
    if i == 2:
        primos.append(i)
    if i == 3:
        primos.append(i)
    if (i % 2) == 0:
        i += 1
    elif (i % 3) == 0:
        i += 1
    else:
        primos.append(i)
        i += 1
# SAIDA
primos = str(primos).strip('[]')
print(primos)