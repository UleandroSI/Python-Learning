#Faça um Programa para leitura de três notas parciais de um aluno. 
#O programa deve calcular a média alcançada por aluno e presentar:
#  a. A mensagem "Aprovado", se a média for maior ou igual a 7, 
# com a respectiva média alcançada;
# b. A mensagem "Reprovado", se a média for menor do que 7, 
# com a respectiva média alcançada;
# c. A mensagem "Aprovado com Distinção", se a média for igual a 10.

#VARIAVEIS
nota = soma = media = 0
#PROCESSAMENTO
nota = float(input("Digite a 1 nota: "))
soma = soma + nota
nota = float(input("Digite a 2 nota: "))
soma = soma + nota
nota = float(input("Digite a 3 nota: "))
soma = soma + nota
media = soma / 3
if media == 10:
    print("Aprovado com Distinçao- %.1f" %media)
elif media >= 7:
    print("Aprovado - %.1f" %media)
elif media < 7:
    print("Reprovado - %.1f" %media)