# O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. 
# Confira:
#                      Até 5 Kg           Acima de 5 Kg
#File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
#Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
#Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
# Para atender a todos os clientes, cada cliente poderá levar apenas um dos 
# tipos de carne da promoção, porém não há limites para a quantidade de carne 
# por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda 
# um desconto de 5% sobre o total da compra. Escreva um programa que peça o 
# tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, 
# contendo as informações da compra: 
#     tipo e quantidade de carne, preço total, tipo de pagamento, 
#     valor do desconto e valor a pagar.

#VARIAVEIS
valor = desconto = total = 0
print("--- Supermecado Tabajara ---\n Escolha uma das opcoes:")
print("1-File Duplo  2-Alcatra  3-Picanha")
tipo = int(input("Digite a opcao escolhida: "))
kilos = int(input("Kilos: "))
#PROCESSAMENTO
if tipo == 1:
    if kilos <= 5:
        valor = 4.9 * kilos
    else:
        valor = 5.8 * kilos
elif tipo == 2:
    if kilos <= 5:
        valor = 5.9 * kilos
    else:
        valor = 6.8 * kilos
else:
    if kilos <= 5:
        valor = 6.9 * kilos
    else:
        valor = 7.8 * kilos

card = input("Pagamento com cartão Tabajara S(Sim): ")
card = card.lower()
if card == 's':
    desconto = valor * 0.05
    total = valor - desconto
else:
    total = valor
#SAIDA
print("------------------------------\n          Cupom Fiscal")
if tipo == 1:
    print("File Duplo - %dKg" %kilos)
elif tipo == 2:
    print("Alcatra - %dKg" %kilos)
else:
    print("Picanha - %dKg" %kilos)
print("Total: R$%.2f" %valor)
print('Cartão Tabajara' if card == 's' else 'Pagamento em Dinheiro')
print("Desconto: R$%.2f" %desconto)
print("Valor a pagar: R$%.2f" %total)
print("------------------------------")