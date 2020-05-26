# O sr. Manoel Joaquim expandiu seus negocios para além dos negocios de 1,99
#e agora possui uma loja de conveniencias. Faça um programa que implemente uma
#caixa registradora rudimentar. O programa devera receber um numero desconhecido
#de valores referente aos preços das mercadorias. Um valor zero deve ser
#informado pelo operador para indicar o final da compra. O programa deve então
#mostrar o final da compra e perguntar o valor em dinheiro que o cliente
#forneceu, para então calcular e mostrar o valor do troco. Apos esta operação,
#o programa devera voltar ao ponto inicial,  para registrar a proxima compra.

#VARIAVEIS
caixa_dia = 0
while True:
    fim = cont = 1
    total = dinheiro = troco = 0
    print("Lojas Tabajara")
#EXECUÇAO
    while True:
        preco = float(input("Produto: %i: R$  " %cont))
        cont += 1
        total += preco
        if preco == 0:
            print("Total desta compra: R$ %.2f" %total)
            break
    dinheiro = float(input("Dinheiro: R$ "))
#SAIDA
    print("Troco: R$ %.2f" %(dinheiro-total))
    print("")
    caixa_dia += total