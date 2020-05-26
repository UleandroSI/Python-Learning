#Faça um programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu
#respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.

#VARIAVEIS
idade = []
altura = []
#PROCESSAMENTO
for x in range(0,5):
    i = int(input("Digite a idade da %d pessoa: " %(x+1)))
    idade.append(i)
    l = m = 1
    while l == m:
        l += 1
        a = int(input("Digite a altura da %d pessoa: "%(x+1)))
        altura.append(a)
#SAIDA
for y in range(4,-1,-1):
    print(idade[y], altura[y])