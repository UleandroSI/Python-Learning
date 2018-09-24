# O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
# Até           5 Kg            Acima de 5 Kg
# File Duplo    R$ 4,90 por Kg      R$ 5,80 por Kg
# Alcatra       R$ 5,90 por Kg      R$ 6,80 por Kg
# Picanha       R$ 6,90 por Kg      R$ 7,80 por Kg
# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não
# há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um
# desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada
# pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total,
# tipo de pagamento, valor do desconto e valor a pagar.

# Entrada
tipo = input("Carne: ")
kilo = float(input("Digite o quilo: "))

# Execuçao
tipo = tipo.upper()
while True:
    if tipo == "FILE DUPLO":
        if kilo <= 5:
            valor = kilo * 4.9
            break
        else:
            valor = kilo * 5.8
            break
    elif tipo == "ALCATRA":
        if kilo <= 5:
            valor = kilo * 5.9
            break
        else:
            valor = kilo * 6.8
            break
    elif tipo == "PICANHA":
        if kilo <= 5:
            valor = kilo * 6.9
            break
        else:
            valor = kilo * 7.8
            break
    else:
        print("Escolha apenas FILE DUPLO - ALCATRA - PICANHA")

cartao = input("Pagar com cartão Tabajara? \n   SIM - NÃO \n: ")
cartao = cartao.upper()
while True:
    if cartao == "SIM":
        desconto = valor * 0.05
        break
    elif cartao == "NÃO":
        desconto = 0
        break
    else:
        print("Digite apenas SIM ou NÃO")
total = valor - desconto

# Saida
print("\n%.10s        %20.1f" %(tipo, kilo))
print(" Valor Total: %20.2f" %valor)
print("Pagamento com cartão da loja: %5s" %cartao)
print('-'*45)
print("Desconto:    %20.2f" %desconto)
print('-'*45)
print('-'*45)
print(" Preço Total: %20.2f" %total)
print('-'*45)