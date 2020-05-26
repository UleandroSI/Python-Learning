# Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
# a. Esse funcionário foi contratado em 1995, com salario de R$1000;
# b. Em 1996 recebeu aumento de 1,5% sobre seu salario inicial;
# c. A partir de 1997(inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior.
# Faça um programa que determine o salario atual desse funcionario. Após concluir isto, altere o programa 
#permitindo que o usuário digite o salario inicial do funcionário.

# Variaveis
ano = 2018
salario = 1000
aumento = 0.015
valor = salario = 0

# Execução
salario = float(input("Digite o salario do funcionario: "))
for x in range(1996,ano):
    valor = salario * aumento
    salario = valor + salario
    print("Salario de %d: R$ %.2f" %(x,(salario)))
    aumento = aumento * 2