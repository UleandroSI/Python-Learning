# Foi feita uma estatistica em cinco cidades brasileiras para coletar dados
#sobre acidentes de transito. Foram obtidos os seguintes dados:
# a) codigo da cidade;
# b) numero de veiculos de passeio em 1999;
# c) numero de acidentes de transito com vitimas em 1999; Deseja-se saber:
# d) Qual o maior e menor indice de acidentes, e a qual cidade pertence;
# e) QUal a media de veiculos na cinco cidades juntas;
# f) Qual a media de acidentes de transito nas cidade com menos de 2000 veiculos.

#VARIAVEIS
codigo_cidade = numero_veiculos = acidentes = maior_indice = 0
media_veiculos = cidade_menor = cidade_maior = cont_i = soma_pequena_cidade = 0
menor_indice = 9999999999

for x in range(1,6):
    codigo_cidade = int(input("Digite o codigo da cidade %d: "%x))
    numero_veiculos = int(input("Digite o numero de veiculos: "))
    media_veiculos += numero_veiculos
    acidentes = int(input("Digite o numero de acidentes com vitimas: "))
    
    if acidentes < menor_indice:
        menor_indice = acidentes
        cidade_menor = codigo_cidade
    if acidentes >= maior_indice:
        maior_indice = acidentes
        cidade_maior = codigo_cidade
    if numero_veiculos < 2000:
        cont_i += 1
        soma_pequena_cidade += acidentes

#SAIDA
print("")
print("O menor indice de acidente: %d da cidade: %d" %(menor_indice,cidade_menor))
print("O maior indice de acidente: %d da cidade: %d" %(maior_indice,cidade_maior))
print("Media de veiculos de todas cidades: %d" %(media_veiculos/5))
if cont_i != 0:
    print("Media de acidentes nas cidades pequenas: %d" %(soma_pequena_cidade/cont_i))
else:
    print("Não houve cidades com menos de 2000 veiculos.")