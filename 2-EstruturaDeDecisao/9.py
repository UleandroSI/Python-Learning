# Faça um Programa que leia três números e mostre-os em ordem decrescente.

# Variaveis
primeiro = segundo = terceiro = 0
produto1 = float(input("Digite o preço do primeiro produto: "))
produto2 = float(input("Digite o preço do segundo produto: "))
produto3 = float(input("Digite o preço do terceiro produto: "))

#Processamento
if produto1 > produto2:
    if produto1 > produto3:
        primeiro = produto1
        if produto2 > produto3:
            segundo = produto2
            terceiro = produto3
        else:
            segundo = produto3
            terceiro = produto2
    else:
        primeiro = produto3
        segundo = produto1
        terceiro = produto2

else:
    if produto2 > produto3:
        primeiro = produto2
        if produto1 > produto3:
            segundo = produto1
            terceiro = produto3
        else:
            segundo = produto3
            terceiro = produto1
    else:
        primeiro = produto3
        segundo = produto2
        terceiro = produto1
# SAIDA
print(primeiro,segundo,terceiro)