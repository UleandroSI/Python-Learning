# Altere o programa de calculo do fatorial, permitindo ao usuario calcular
# o fatorial varias vezes e limitando o fatorial a numeros inteiros
# positivos e menores que 16.

# VARIÁVEIS
op = ''

# EXECUÇÃO
while True:
    num = int(input("Digite o numero: "))
    i = num
    fatorial = num
    var1 = []
    
    while i > 1:
        var1.append(i)
        fatorial = fatorial * (i-1)
        i -= 1
        
    var1.append(1)
    print("Fatorial de %i! = %s = %i" %(num, var1,fatorial))
    
    op = input("Para sair digite 's': ")
    if op == 's':
        print("Sair")
        break
    else:
        print("Continuar")