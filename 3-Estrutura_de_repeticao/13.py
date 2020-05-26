# Faça um programa que peça dois numeros, base e expoente, calcule e 
# mostre o primeiro numero elevado ao segundo. Não utilize a função de 
# potencia da linguagem.

i = 1
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

total = num1
while i < num2:
    total = total * num1
    i += 1

print(total)