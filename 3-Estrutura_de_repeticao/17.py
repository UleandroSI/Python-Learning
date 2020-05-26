# Faça um programa que calcule o fatorial de um numero inteiro
# fornecido pelo usuario. Ex. 5! = 5.4.3.2.1 = 120

# VARIÁVEIS
num = int(input("Digite o nÃºmero: "))
i = num
fatorial = num
var1 = []

# EXECUÇÃO
while i > 1:
    var1.append(i)
    fatorial = fatorial * (i-1)
    i -= 1

var1.append(1)
# SAÍDA
print("Fatorial de %i! = %s = %i" %(num, var1,fatorial))