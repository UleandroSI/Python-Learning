# Faça um Programa que peça dois números e imprima o maior deles.

# Variaveis
num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundoo numero: "))
# Processamento
if num1 == num2:
    print("Numeros iguais.")
elif num2 > num1:
    print("Maior é: ",num2)
else:
    print("Maior é: ",num1)