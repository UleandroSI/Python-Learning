#Em uma eleicao presidencial existem quatro candidatos.
#Os votos sao informados por meio de codigo.
#Os codigos sao: 1-Jose,2-Joao,3-Fulano,4-Ciclano,5-Nulo,6-Branco
#Calcule e mostre o total de votos para cada candidato;
#Total de votos nulos; Total de votos brancos;Percentagem de votos nulos
#Percentagem de votos brancos. Para finalizar codigo zero.

#VARIAVEIS
cand1 = cand2 = cand3 = cand4 = vb = vn = voto = i = 0
#EXECUCAO
while True:
    print("Codigo - Candidatos:\n  1 -      Jose\n  2 -      Joao\n  3 -      Fulano\n  4 -      Ciclano\n  5 -      Nulo\n  6 -      Branco")
    voto = int(input("Numero candidato: "))
    if voto == 0:
        break
    elif voto == 1:
        cand1 += 1
    elif voto == 2:
        cand2 += 1
    elif voto == 3:
        cand3 += 1
    elif voto == 4:
        cand4 += 1
    elif voto == 5:
        vn += 1
    elif voto == 6:
        vb += 1
    else:
        pass
    i += 1
#SAIDA
print("Total de votos:")
print("Jose = %10d\nJoao = %10d\nFulano = %8d\nCiclano = %7d\n"%(cand1,cand2,cand3,cand4))
print("Total votos Nulos = %10d - Percentagem = %d"%(vn,(vn/i)*100))
print("Total votos Brancos = %8d - Percentagem = %d"%(vb,(vb/i)*100))