# Faça um programa que calcule o valor total investido por um colecionador
#em sua coleção de CDs e o valor medio gasto em cada um deles.
# O usuario devera informar a quantidade de CDs e o valor de cada um.

#VARIAVEIS
cd = valor = media = soma = 0
cd = int(input("Digite a quantidade de CDs: "))

#EXECUÇAO
for x in range(1, (cd+1)):
    valor = float(input("Digite o valor do CD %i:" %x))
    soma += valor
media = soma / cd

#SAIDA
print("Total e CDs: %i" %cd)
print("Total e gasto: %.2f" %soma)
print("Media por CD: %.2f" %media)