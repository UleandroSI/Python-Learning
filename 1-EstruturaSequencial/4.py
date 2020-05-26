# Faça um programa que peça as 4 notas bimestrais e mostre a media.

#Variaveis
bim1 = bim2 = bim3 = bim4 = 0

#PRocessamento
bim1 = float(input("Digite a nota do primeiro bimestre: "))
bim2 = float(input("Digite a nota do segundo bimestre: "))
bim3 = float(input("Digite a nota do terceiro bimestre: "))
bim4 = float(input("Digite a nota do quarto bimestre: "))
media = (bim1 + bim2 + bim3 + bim4)/4

#Saida
print("A media desse aluno foi: ", media)