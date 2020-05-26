# Faça um programa que calcule o numero medio de alunos por turma.
# Para isto, peça a quantidade de turmas e a quantidade de alunos para
# cada turma. As turmas não podem ter mais de 40 alunos.

# VARIAVEIS
cont = media = 0
turmas = int(input("Digite o numero de turmas: "))

# EXECUÇAO
for x in range(1,(turmas+1)):
    while True:
        alunos = int(input("Digite a quantidade de alunos da turma %i: " %x))
        if alunos <= 40:
            break
    cont += alunos    
media = cont / turmas

# SAIDA
print("A media de alunos é: %i" %media)