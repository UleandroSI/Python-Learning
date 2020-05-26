# Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que 
# determine quantos alunos com mais de 13 anos possuem altura inferior à 
# média de altura desses alunos.

#VARIAVEIS
idade = []
altura = []
media = cont = soma = 0

#PROCESSAMENTO
for x in range(0,30):
    i = int(input("Digite a idade do %d aluno: " %(x+1)))
    idade.append(i)
    a = float(input("Digite a altura do %d aluno: " %(x+1)))
    altura.append(a)
    soma += a
media = soma / 30
for y in range(0,30):
    if idade[y] >= 13:
        if altura[y] < media:
            cont += 1

#SAIDA
print("Media de altura: ", media)
print("Alunos com altura inferior a media: ", cont)