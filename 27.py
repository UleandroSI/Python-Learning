# Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#               Até 5 Kg              Acima de 5 Kg
# Morango       R$ 2,50 por Kg         R$ 2,20 por Kg
# Maçã          R$ 1,80 por Kg         R$ 1,50 por Kg
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um
# desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade
# (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

# Entrada
morango = float(input("Digite o quilo do Morango: "))
maca = float(input("Digite o quilo da Maçã: "))

# Execuçao
kilo = maca + morango
if morango < 5.0:
    valMorango = morango * 2.5
else:
    valMorango = morango * 2.2
if maca < 5.0:
    valMaca = maca * 1.8
else:
    valMaca = maca * 1.5
valor = valMaca + valMorango

if kilo > 8.0 or valor > 25.0:
    total = valor - (valor * 0.01)
else:
    total = valor

# Saida
print("\n Morango: %.1f Kg" %morango)
print(" Maçã:  %.1f Kg" %maca)
print("Valor a pagar: R$ %.2f" %total)