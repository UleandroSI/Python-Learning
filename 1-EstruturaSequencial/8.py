# Faça um Programa que pergunte quanto você ganha por hora e o 
#número de horas trabalhadas no mês. Calcule e mostre o total do seu salário.

# Variaveis
valor = float(input("Digite o valor por hora: "))
horas = int(input("Digite o numero de horas: "))
# Processamento
salario = valor * horas
# Saida
print("Total do salario: R$ %.2f" %salario)