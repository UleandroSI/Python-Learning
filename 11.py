# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# a. o produto do dobro do primeiro com metade do segundo .
# b. a soma do triplo do primeiro com o terceiro.
# c. o terceiro elevado ao cubo.

# Entradas
i1 = int(input("Digite o primeiro inteiro: "))
i2 = int(input("Digite o segundo inteiro: "))
r = float(input("Digite o numero real: "))

# Execuçao
a = (i1 * 2) + (i2 / 2)
b = float(i1 * 3) + r
c = (r * r) * r

# Saidas
print("Resposta A: %d" %a)
print("Resposta B: %d" %b)
print("Resposta C: %d" %c)