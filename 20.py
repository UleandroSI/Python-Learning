# Faça um Programa para leitura de três notas parciais de um aluno.
# O programa deve calcular a média alcançada por aluno e apresentar:
# a. A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
# b. A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
# c. A mensagem "Aprovado com Distinção", se a média for igual a 10.

# Entrada
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Execuçao
media = (nota1 + nota2 + nota3) / 3
if media >= 7:
    if media == 10:
        print("Aprovado com Distinção. %10.1f" %media)
    else:
        print("Aprovado. %10.1f" % media)
elif media <7:
    print("Reprovado. %10.1f" % media)