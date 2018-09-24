# Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo.
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
# Dicas:
# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes;

# Entrada
lado1 = float(input("Digite o primeiro lado: "))
lado2 = float(input("Digite o segundo lado: "))
lado3 = float(input("Digite o terceiro lado: "))

# Execuçao
if lado1 + lado2 > lado3 or lado2 + lado3 > lado1 or lado1 + lado3 > lado2:
    triangulo = True

if triangulo == True:
    if lado1 == lado2 and lado1 == lado3:
        tipo = "Equilatero"
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        tipo = "Isoceles"
    else:
        tipo = "Escaleno"

# Saida
print("Este triângulo é: %s" %tipo)