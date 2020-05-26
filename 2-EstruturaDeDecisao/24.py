# Faça um Programa que leia 2 números e em seguida pergunte ao usuário 
# qual operação ele deseja realizar. O resultado da operação deve ser 
# acompanhado de uma frase que diga se o número é:
#  a. par ou ímpar;
#  b. positivo ou negativo;
#  c. inteiro ou decimal.

#VARIAVEIS
pnumero = float(input("Digite o primeiro numero: "))
snumero = float(input("Digite o segundo numero: "))
print("1- par ou ímpar;\n2- positivo ou negativo;\n3- inteiro ou decimal.")
opc = int(input("Digite sua opcao: "))

#PROCESSAMENTO
if opc == 1:
    if pnumero % 2 == 0:
        print("Primeiro Numero par")
    else:
        print("Primeiro Numero impar")
    if snumero % 2 == 0:
        print("Segundo Numero par")
    else:
        print("Segundo Numero impar")
elif opc == 2:
    if pnumero < 0:
        print("Primeiro Numero negativo.")
    else:
        print("Primeiro Numero positivo")
    if snumero < 0:
        print("Segundo Numero negativo.")
    else:
        print("Segundo Numero positivo")
elif opc == 3:
    if pnumero == round(pnumero):
        print("Primeiro Numero inteiro.")
    else:
        print("Primeiro Numero decimal")
    if snumero == round(snumero):
        print("Segundo Numero inteiro.")
    else:
        print("Segundo Numero decimal")
else:
    print("Numero invalido.")