# '''Reverso do número.''' Faça uma função que retorne o reverso de um 
# número inteiro informado. Por exemplo: 127 -> 721.

# VARIAVEIS
def reverso(numero):
    converter = str(numero)
    string = converter[::-1]
    numero = int(string)
    return numero

# PROCESSAMENTO
numero = int(input("Digite um numero: "))
invertido = reverso(numero)

# SAIDA
print("Numero reverso: %d" %invertido)