#Faça um programa que receba o valor de uma divida e mostre uma tabela
# com os seguintes dados: valor da divida, valor dos juros,
# quantidade de parcelas, e valor da parcela.
# Os juros e a quantidade de parcelas são tabeladas:
# Quantidade de Parcelas            % Juros sobre valor inicial da divida
#           1                                       0
#           3                                       10
#           6                                       15
#           9                                       20
#           12                                      25

#VARIAVEIS
juros = valor = 0
i = 1
j = 0.1
divida = float(input("Digite o valor da divida: R$ "))
print("Valor da Divida  Valor dos Juros     Quantidade de Parcelas  Valor da Parcela")
print("%.2f         %10.2f           %10d             %10.2f" %(divida, juros, i, divida))
for x in range(3, 13, 3):
    juros = divida * j
    j += 0.05
    parcela = divida + juros
    valor = parcela / x
    print("%.2f         %10.2f           %10d            %10.2f"%(parcela,juros,x,valor))