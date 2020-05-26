#Faça um programa que leia uma quantidade indeterminada de numeros 
# positivos e conte quantos deles estão nos seguintes intervalos:
# [0-25], [26-50], [51-75], [76-100]. A entrada de dados terminara
# quando for dada entrade de um numero negativo.

#VARIAVEIS
numero = 0
l1 = l2 = l3 = l4 = 0
while True:
    numero = int(input("Digite um numero: "))
    if numero < 0:
        break
    elif numero <= 25:
        l1 += 1
    elif numero <= 50:
        l2 += 1
    elif numero <= 75:
        l3 += 1
    elif numero <= 100:
        l4 += 1
        
#SAIDA
print("")
print("Intervalo [0-25]: %11d \nIntervalo [26-50]: %10d \nIntervalo [51-75]: %10d \nIntervalo [76-100]: %9d \n" %(l1,l2,l3,l4))