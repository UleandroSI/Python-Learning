# Faça um programa que dado um conjunto de N numeros, determine o menor valor,
# o maior valor, e a soma dos valores.
menor = 99999999999999
maior = soma = 0

while True:
    num = float(input("Digite o número: "))
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