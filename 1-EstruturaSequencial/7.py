# Faça um programa que calcule a area de um quadrado, em seguida mostre
#o dobro dessa area para o usuario.

#Variaveis
lado = area = dobro = 0

#PRocessamento
lado = float(input("Digite o valor do lado do quadrado em centimetros: "))
area = lado*lado
dobro = area * area

#Saida
print("O dobro da area e: ",dobro)