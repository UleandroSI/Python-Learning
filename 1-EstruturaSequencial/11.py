# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#  a. o produto do dobro do primeiro com metade do segundo .
#  b. a soma do triplo do primeiro com o terceiro.
#  c. o terceiro elevado ao cubo.

# Variaveis
a = b = c = 0
n1 = int(input("Digite o primeiro numero inteiro: "))
n2 = int(input("Digite o segundo numero inteiro: "))
n3 = float(input("Digite o numero real: "))
# Processamento
a = ((n1 * 2)* (n2 / 2))
b = ((n1 * 3)+ n3)
p = (n3 * n3)
c = p * p
# Saida
print("a)- %i" %a)
print("b)- %i" %b)
print("c)- ",c)