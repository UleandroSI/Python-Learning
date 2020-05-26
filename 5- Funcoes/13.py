# '''Desenha moldura'''. Construa uma função que desenhe um retângulo usando 
# os caracteres ‘+’ , ‘−’ e ‘| ‘. Esta função deve receber dois parâmetros, 
# ''linhas'' e ''colunas'', sendo que o valor por omissão é o valor mínimo 
# igual a 1 e o valor máximo é 20. Se valores fora da faixa forem informados, 
# eles devem ser modificados para valores dentro da faixa de forma elegante.

# VARIAVEIS
def moldura(linhas, colunas):
    for i in range(0, 1):
        print('+' + (('-')*colunas) +'+')
        for y in range(0, linhas):
            print('|' + (' '*colunas) + '|')
        for x in range(0,1):
            print('+' + (('-')*colunas) +'+')

# PROCESSAMENTO
linhas = int(input("Digite o numero de linhas: "))
colunas = int(input("Digite o numero de colunas: "))
if linhas < 1:
    linhas = 1
if linhas > 20:
    linhas = 20
if colunas < 1:
    colunas = 1
if colunas > 20:
    colunas = 20

retorno = moldura(linhas, colunas)