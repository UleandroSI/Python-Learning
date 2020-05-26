# Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais:
# taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um
# item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.

def somaImposto(taxaImposto,custo):
    taxa = (taxaImposto / 100) + 1
    custo = custo * taxa
    print("Novo valor: R$%.2f" %custo)
#PROCESSAMENTO
taxaImposto = int(input("Digite a taxa: "))
custo = float(input("Digite o custo do produto: "))
somaImposto(taxaImposto,custo)
