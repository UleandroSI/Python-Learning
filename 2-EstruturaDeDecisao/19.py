#Faça um Programa que leia um número inteiro menor que 1000 e imprima a 
#quantidade de centenas, dezenas e unidades do mesmo.  
#  Observando os termos no plural a colocação do "e", da vírgula entre outros.
#   Exemplo:
#  a. 326 = 3 centenas, 2 dezenas e 6 unidades
#  a. 12  = 1 dezena e 2 unidades
#  Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10,
#  21, 11, 1, 7 e 16

while True:
    numero = int(input("Digite um numero inteiro: "))
    if numero < 1000:
        break
    else:
        print("Digite um numero menor que 1000(mil).")
n = str(numero)
