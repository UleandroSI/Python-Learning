# Fa�a um programa que calcule o fatorial de um numero inteiro
# fornecido pelo usuario. Ex. 5! = 5.4.3.2.1 = 120

# VARI�VEIS
num = int(input("Digite o número: "))
i = num
fatorial = num
var1 = []

# EXECU��O
while i > 1:
    var1.append(i)
    fatorial = fatorial * (i-1)
    i -= 1

var1.append(1)
# SA�DA
print("Fatorial de %i! = %s = %i" %(num, var1,fatorial))