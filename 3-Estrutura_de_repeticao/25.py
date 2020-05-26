# Faça um programa que peça para N pessoas a sua idade.
# ao final o programa devera verificar se a media de idade da turma
# varia de 0 e 25,26 e 60 e maior que 60; e então dizer se a turma é 
# jovem adulta ou idosa.

# VARIAVEIS
idade = cont = 0
opc = ''

#EXECUÇAO
while True:
    n = int(input("Digite a sua idade: "))
    idade += n
    cont += 1
    
    opc = input("Digite S para sair: ")
    opc = opc.lower()
    if opc == 's':
        break
media = idade / cont

#SAIDA
if media < 1 and media <= 25:
    print("Media de idade jovem: %ianos" %media)
elif media >= 26 and media <= 60:
    print("Media de idade adulta: %ianos" %media)
else:
    print("Media de idade idosa: %ianos" %media)