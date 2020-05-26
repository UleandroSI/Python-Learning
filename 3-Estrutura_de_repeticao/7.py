# Faça um programa que leia 5 numeros e informe o maior

a = maior = 0

for x in range(1,6):
    a = float(input("Digite o %x° numero: " %x))
    if a > maior:
        maior = a
        
print("Maior numero encontrado: ", maior)