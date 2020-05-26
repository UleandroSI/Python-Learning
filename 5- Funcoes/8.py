# Faça uma função que informe a quantidade de dígitos de um determinado 
# número inteiro informado.

# VARIAVEIS
def digitos(numero):
    converter = str(numero)
    quantidade = len(converter)
    return quantidade

# PROCESSAMENTO
numero = int(input("Digite um numero: "))
quantidade = digitos(numero)

# SAIDA
print("Quantidade de digitos do numero: %d" %quantidade)