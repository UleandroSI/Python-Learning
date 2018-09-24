# Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades
# do mesmo.
# Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
# 326 = 3 centenas, 2 dezenas e 6 unidades
# 12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

# Ficou um código grande, pois, eu quis fazer o exercicio sem calculos, e transformando as variáveis.
# Entrada
numero = input("Digite um numero inteiro, menor que 1000 somente: ")

# Execuçao
if numero.isnumeric():
    numero = int(numero)
    if numero > 0 and numero < 999:
        alt = str(numero)
        if numero > 99:
            centena = alt[0]
            dezena = alt[1]
            unidade = alt[2]
            if centena != '1':
                c = "centenas"
                if dezena != '0' and dezena != '1':
                    d = "dezenas"
                    if unidade != '0' and unidade != '1':
                        u = "unidades"
                    else:
                        u = "unidade"
                else:
                    d = "dezena"
                    if unidade != '0' and unidade != '1':
                        u = "unidades"
                    else:
                        u = "unidade"
            else:
                c = "centena"
                if dezena != '0' and dezena != '1':
                    d = "dezenas"
                    if unidade != '0' and unidade != '1':
                        u = "unidades"
                    else:
                        u = "unidade"
                else:
                    d = "dezena"
                    if unidade != '0' and unidade != '1':
                        u = "unidades"
                    else:
                        u = "unidade"
        elif numero > 9:
            centena = '0'
            c = "centena"
            dezena = alt[0]
            unidade = alt[1]
            if dezena != '0' and dezena != '1':
                d = "dezenas"
                if unidade != '0' and unidade != '1':
                    u = "unidades"
                else:
                    u = "unidade"
            else:
                d = "dezena"
                if unidade != '0' and unidade != '1':
                    u = "unidades"
                else:
                    u = "unidade"
        else:
            centena = '0'
            c = "centena"
            dezena = '0'
            d = "dezena"
            unidade = numero
            if unidade != 1:
                u = "unidades"
            else:
                u = "unidade"

        print("%d = %s %s, %s %s e %s %s." %(numero, centena, c, dezena, d, unidade, u))
    else:
        print("Numero invalido.")