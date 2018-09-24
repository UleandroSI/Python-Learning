#  Faça um Programa que leia três números e mostre o maior deles.

# Entrada
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o Terceiro número: "))

# Execução
if n1 > n2:
    if n1 > n3:
        print("O maior é: %d" %n1)
    else:
        print("O maior é: %d" %n3)
else:
    if n2 > n3:
        print("O maior é: %d" %n2)
    else:
        print("O maior é: %d" % n3)
