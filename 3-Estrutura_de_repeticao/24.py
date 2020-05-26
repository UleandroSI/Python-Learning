# Faça um programa que mostre a média aritimetica de N notas.

# VARIAVEIS
notas = cont = 0
opc = ''

#EXECUÇAO
while True:
    n = float(input("Digite a nota: "))
    notas += n
    cont += 1
    
    opc = input("Digite S para sair: ")
    opc = opc.lower()
    if opc == 's':
        break
media = notas / cont

#SAIDA
print("Media das notas digitadas: %.2f" %media)