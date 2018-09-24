# Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar
# quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é
# de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na
# máquina.
# Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de
# 5 e uma nota de 1;
# a.
# Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas
# de 10, uma nota de 5 e quatro notas de 1.

# Entrada
nota100 = 0
nota50 = 0
nota10 = 0
nota5 = 0
nota1 = 0
while True:
    valor = int(input("Digite o valor do saque: "))
    if valor < 10 or valor > 600:
        print("Valor deve estar entre 10 e 600 reais.")
    else:
        break
# Execução
saque = valor
while saque >= 100:
    nota100 += 1
    saque = saque - 100
while saque >= 50:
    nota50 += 1
    saque = saque - 50
while saque >= 10:
    nota10 += 1
    saque = saque - 10
while saque >= 5:
    nota5 += 1
    saque = saque - 5
while saque >= 1:
    nota1 += 1
    saque = saque - 1

# Saida
print('-' * 30)
print("Valor do saque: R$ %10d" %valor)
print("Notas 100- %d, 50- %d, 10- %d, 5- %d, 1- %d" %(nota100, nota50, nota10, nota5, nota1))