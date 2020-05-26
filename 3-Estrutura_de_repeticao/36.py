# Desenvolva um programa que faça a tabuada de um numero qualquer inteiro que 
#sera digitado pelo usuário,mas a tabuada não deve necessariamente iniciar 
#em 1 e terminar em 10, o valor inicial e final devem ser informados 
#tambem pelo usuário.

# Variaveis
while True:
	tabuada = int(input("Montar a tabuada de: "))
	inicial = int(input("Começar com: "))
	final = int(input("Terminar em: "))
	if inicial > final:
		print("O começo deve ser menor que o final.")
	else:
		break

# Execuçao
print(" ")
print("Vou montar a tabuada do %d começando em %d e terminando em %d: " %(tabuada,inicial,final))
for x in range(inicial,final+1):
	print("%d x %d = %d" %(tabuada, x, (tabuada*x)))