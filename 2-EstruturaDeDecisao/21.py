# Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao 
# usuário a valor do saque e depois informar quantas notas de cada valor 
# serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. 
# O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve 
# se preocupar com a quantidade de notas existentes na máquina.
#   a. Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas 
# notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
#   b. Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três 
# notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

#VARIAVEIS
cont_100 = cont_50 = cont_10 = cont_5 = cont_1 = 0
valor = 0
while True:
    saque = float(input("Digite o valor do saque: "))
    if saque < 10 or saque > 600:
        print("Valor invalido")
    else:
        break
#PROCESSAMENTO
valor = saque
while True:
    if valor >= 100:
        cont_100 += 1
        valor -= 100
    elif valor >= 50:
        cont_50 += 1
        valor -= 50
    elif valor >= 10:
        cont_10 += 1
        valor -= 10
    elif valor >= 5:
        cont_5 += 1
        valor -= 5
    elif valor >= 1:
        cont_1 += 1
        valor -= 1
    else:
        break

#SAIDA
print("Saque de valor: R$%.2f" %saque)
print("Notas de 100: ",cont_100)
print("Notas de 50: ",cont_50)
print("Notas de 10: ",cont_10)
print("Notas de 5: ",cont_5)
print("Notas de 1: ",cont_1)