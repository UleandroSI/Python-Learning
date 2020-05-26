#Faça um programa que leia o codigo dos itens e quantidade desejada
# Calcule e mostre o valor a ser pago por item(preco*quantidade)
# e o total geral do pedido. Considere que o cliente deve informar
# quando o pedido deve ser encerrado.

#VARIAVEIS
codigo = quantidade = valor = total = 0
compra = []
prod1 = ['Cachorro quente', 1.2]
prod2 = ['Bauru simples', 1.3]
prod3 = ['Bauru com ovo', 1.5]
prod4 = ['Hamburger', 1.2]
prod5 = ['Cheeseburger', 1.3]
prod6 = ['Refrigerante', 1.0]

#EXECUCAO
while True:
    print("Especificacao    Codigo  Preco")
    print("Cachorro quente  100     1.20")
    print("Bauru simples    101     1.30")
    print("Bauru com ovo    102     1.50")
    print("Hamburger        103     1.20")
    print("Cheeseburger     104     1.30")
    print("Refrigerante     105     1.00")
    while True:
        codigo = int(input("Codigo: "))
        quantidade = int(input("Quantidade: "))
        if codigo == 100:
            valor = 1.20 * quantidade
            total += valor
            print("%s   R$%.2f  Valor = R$%.2f" %(prod1[0], prod1[1],valor))
        elif codigo == 101:
            valor = 1.30 * quantidade
            total += valor
            print("%s   R$%.2f  Valor = R$%.2f" %(prod2[0], prod2[1],valor))
        elif codigo == 102:
            valor = 1.50 * quantidade
            total += valor
            print("%s   R$%.2f  Valor = R$%.2f" %(prod3[0], prod3[1],valor))
        elif codigo == 103:
            valor = 1.20 * quantidade
            total += valor
            print("%s   R$%.2f  Valor = R$%.2f" %(prod4[0], prod4[1],valor))
        elif codigo == 104:
            valor = 1.30 * quantidade
            total += valor
            print("%s   R$%.2f  Valor = R$%.2f" %(prod5[0], prod5[1],valor))
        elif codigo == 105:
            valor = 1.0 * quantidade
            total += valor
            print("%s   R$%.2f  Valor = R$%.2f" %(prod6[0], prod6[1],valor))
        else:
            break
        
#SAIDA
    print("Total____________________________ = R$%.2f\n"%total)