# Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da
# operação deve ser acompanhado de uma frase que diga se o número é:
# a. par ou ímpar;
# b. positivo ou negativo;
# c. inteiro ou decimal.

# Entrada
num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))
print(" 1 - Soma")
print(" 2 - Subtração")
print(" 3 - Multiplicação")
print(" 4 - Divisão")
op = int(input("Escolha qual operação deseja fazer: "))

# Execução
if op == 1:
    resultado = num1 + num2
    if resultado % 2 == 0:
        a = "par"
    else:
        a = "impar"
    if resultado >= 0:
        b = "positivo"
    else:
        b = "negativo"
    if int(resultado) == resultado:
        c = "inteiro"
    else:
        c = "decimal"
elif op == 2:
    resultado = num1 - num2
    if resultado % 2 == 0:
        a = "par"
    else:
        a = "impar"
    if resultado >= 0:
        b = "positivo"
    else:
        b = "negativo"
    if int(resultado) == resultado:
        c = "inteiro"
    else:
        c = "decimal"
elif op == 3:
    resultado = num1 * num2
    if resultado % 2 == 0:
        a = "par"
    else:
        a = "impar"
    if resultado >= 0:
        b = "positivo"
    else:
        b = "negativo"
    if int(resultado) == resultado:
        c = "inteiro"
    else:
        c = "decimal"
elif op == 4:
    resultado = num1 / num2
    if resultado % 2 == 0:
        a = "par"
    else:
        a = "impar"
    if resultado >= 0:
        b = "positivo"
    else:
        b = "negativo"
    if int(resultado) == resultado:
        c = "inteiro"
    else:
        c = "decimal"
else:
    print("Opção invalida.")

# Saida
print("Resultado: %.1f" %resultado)
print("a. %s" %a)
print("b. %s" %b)
print("c. %s" %c)