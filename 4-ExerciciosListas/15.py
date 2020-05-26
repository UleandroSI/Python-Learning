# Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada
# de dados quando for informado um valor igual a -1(que não deve ser armazenado). Após esta entrada de dados

# a)Mostre a quantidade de valores que foram lidos;
# b)Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
# c)Exiba todos os valores na ondem inversa à que foram informados, um abaixo do outro;
# d)Calcule e mostre a soma dos valores;
# e)Calcule e mostre a média dos valores;
# f)Calcule e mostre a quantidade e valores acima da média calculada;
# g)Calcule e mostre a quantidade de valores abaixo de sete;
# h)Encerre o programa com uma mensagem;

# Variaveis
numeros = []
entrada = 0
cont = 1
x = i = soma = media = acima = abaixo = 0
acima_media = []
abaixo_media = []

# Execuçao
print("Digite as Notas, com números positivos. Ou digite -1 para encerrar.")
while True:
	entrada = float(input("Digite o %dº número: " %cont))
	cont += 1
	if entrada == -1:
		break
	else:
		numeros.append(entrada)

# a)Mostre a quantidade de valores que foram lidos;
print("Foram lidas %d notas." %len(numeros))

# b)Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
print(numeros)

# c)Exiba todos os valores na ondem inversa à que foram informados, um abaixo do outro;
y = len(numeros)-1
while y >= 0:
	print(numeros[y])
	soma = soma + numeros[y] # d)Calcule e mostre a soma dos valores;
	y -= 1

# d)Calcule e mostre a soma dos valores;
print("A soma das notas é: %.2f" %soma)

# e)Calcule e mostre a média dos valores;
media = soma / len(numeros)
print("A média é: %.2f" %media)

# f)Calcule e mostre a quantidade e valores acima da média calculada;
i = len(numeros)-1
while i >= 0:
	if numeros[i] > media:
		acima += 1
		acima_media.append(numeros[i])
	else:
		abaixo += 1
		abaixo_media.append(numeros[i])
	i -= 1
print("Numeros acima da média: %s" %acima_media)

# g)Calcule e mostre a quantidade de valores abaixo de sete;
print("Numeros abaixo da média: %s" %abaixo_media)

# h)Encerre o programa com uma mensagem;
print("Obrigado por utilizar o programa.")