# Em uma competição de salto em distancia cada atleta tem direito a 5 saltos.
#No final da serie de saltos de cada atleta, o melhor e pior resultado são
#eliminados. O seu resultado fica sendo a media dos 3 valores restantes.
#Voce deve fazer um programa que receba o nome e as cinco distancias alcançadas
#pelo atleta e depois informe a media dos saltos. Faça uso de uma lista para 
#armazenar os saltos. Os saltos são armazenados na ordem de execução, portanto
#não são ordenados. O programa deve ser encerrado quando não for informado o 
#nome do atleta. A saida do programa deve ser conforme o exemplo:
# Atleta: Rodrigo Saltador
# 
# Primeiro salto: 6.5 m
# Segundo salto: 6.1 m
# Tereceiro salto: 6.2 m
# Quarto salto: 5.4 m
# Quinto salto: 5.3 m

# Melhor salto: 6.5
# Pior salto: 5.3
# Media dos demais saltos: 5.9 m

# Resultado final: 
# Rodrigo Saltador: 5.9 m

# Variaveis
dados = []
nome_atleta = ''
notas = 0

# Execucao
while True:
    nome_atleta = input("Nome do atleta: ")
    if nome_atleta == '':
        print("Encerrando \n")
        break
    else:
        dados.append(nome_atleta)
    notas = float(input("Digite a nota: "))
    dados.append(notas)
        
# Saida
