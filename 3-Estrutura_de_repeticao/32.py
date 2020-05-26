#Faça um progrma que calcule o fatorial de um numero inteiro
# fornecido pelo usuario. Ex.: 5! = 5.4.3.2.1=120. A saida deve ser como
# exemplo: 5! = 5.4.3.2.1 = 120

# VARIÁVEIS
num = int(input("Digite o nÃºmero: "))
i = num
fatorial = num
var1 = saida = []

# EXECUÇÃO
while i > 1:
    var1.append(i)
    fatorial = fatorial * (i-1)
    i -= 1

var1.append(1)
#saida = str(var1).strip('[]')
# SAÍDA
saida = '.'.join(map(str,saida))
print("Fatorial de %i! = %s = %i" %(num, saida,fatorial))