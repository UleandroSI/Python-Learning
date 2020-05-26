# A série de Fibonacci é formada pela sequência 1,1,2,3,5,8,13,21,34,55...
# Faça um programa capaz de gerar a série até o n-ésimo termo.

i = 0
n = int(input('Digite a quantidade de termos: '))
a = 1
b = 1
var = []

while i <= n-1:
    var.append(a)
    a,b = b, a + b
    i += 1

print(var)