# Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica:
# utilize uma função de arredondamento.

# Entrada
numero = float(input("Digite um numero: "))

# Execuçao
if int(numero) == numero:
    print("Numero inteiro.")
else:
    print("Numero decimal.")