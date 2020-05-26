# Faça um Programa que peça os 3 lados de um triângulo. O programa deverá 
#informar se os valores podem ser um triângulo. Indique, caso os lados 
#formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno. 
#   Dicas:
#   a. Três lados formam um triângulo quando a soma de quaisquer dois lados 
#  for maior que o terceiro;
#   a. Triângulo Equilátero: três lados iguais;
#   a. Triângulo Isósceles: quaisquer dois lados iguais;
#   a. Triângulo Escaleno: três lados diferentes;

#Variaveis
triangulo = False
lado1 = float(input("Digite o primeiro lado: "))
lado2 = float(input("Digite o segundo lado: "))
lado3 = float(input("Digite o terceiro lado: "))
# Processamento
if lado1 + lado2 > lado3:
    triangulo = True
elif lado1 + lado3 > lado2:
    triangulo = True
elif lado2 + lado3 > lado1:
    triangulo = True
else:
    print("Nao e um triangulo.")
    
if triangulo:
    if lado1 == lado2:
        if lado1 == lado3:
            print("Triângulo Equilátero")
        else:
            print("Triângulo Isosceles")
    elif lado1 == lado3:
        print("Triângulo Isosceles")
    elif lado2 == lado3:
        print("Triângulo Isosceles")
    else:
        print("Triângulo Escaleno")