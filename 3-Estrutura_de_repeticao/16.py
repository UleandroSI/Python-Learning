# A série de Fibonacci é formada pela sequência 0,1,1,2,3,5,8,13,21,34,55...
# Faça um programa capaz de gerar a série até o valor seja maior que 500.

i = 0
a = 0
b = 1
var = []

while a < 500:
    a,b = b, a + b
    var.append(a)

print(var)