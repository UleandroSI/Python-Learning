# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o
# total do seu salário no referido mês.

# Entrada
valor = float(input("Quanto você ganha por hora: "))
horas = float(input("Numero de horas trabalhadas: "))

# Calculo
salario = valor * horas

# Saida
print("O salario do mês é: R$%.2f" %salario)