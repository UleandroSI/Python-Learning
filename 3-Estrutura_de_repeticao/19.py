# Altere o programa anterior para que ele aceite apenas numeros
# entre 0 e 1000.

menor = 1001
maior = soma = 0

while True:
    while True:
        num = float(input("Digite o número: "))
        if num > 0 and num < 1000:
            break
    if menor > num:
        menor = num
    if maior < num:
        maior = num
    soma += num
    
    escolha = input("Para sair digite 's': ")
    if escolha == 's':
        break
print("O menor valor é: %10.2f" %menor)
print("O maior valor é: %10.2f" %maior)
print("A soma é: %17.2f" %soma)