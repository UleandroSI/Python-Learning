# Faça um programa que leia e valide as seguintes informações:
# a)Nome: maior que 3 caracteres;
# b)Idade: entre 0 e 150;
# c)Salário: maior que zero;
# d)Sexo: 'f' ou 'm';
# e)Estado Civil: 's', 'c', 'v', 'd';



while True:
    nome = input("Digite seu nome: ")
    if 3 < len(nome):
        break
    else:
        print('Nome deve conter mais que 3 caracteres!')
        
while True:
    idade = int(input("Digite sua idade: "))
    if idade not in range(0,151):
    	print('Idade deve ser entre 0 e 150 anos!')
    else:
    	break
print(' ')
while True:
	salario = float(input('Digite seu salario: '))
	if salario <= 0:
		print('Salário deve ser maior que 0!')
	else:
		break
print(' ')
x = ['f','m']
while True:
	sexo = input('Sexo Masculino (m), ou Feminino (f): ')
	if sexo not in x:
		print('Utilize m para Masculino e f para Feminino!')
	else:
		break
print(' ')
estado = ['s', 'c', 'v', 'd']
while True:
	print('Digite seu estado civil. Utilize (s)Solteiro(a), (c)Casado(a), (v)Viúvo(a), (d)Disquitado(a).')
	civil = input(': ')
	if civil not in estado:
		print('Digite seu estado civil. Utilize apenas s, c, v, d!')
	else:
		break
print(' ')
print('Nome: %s' %nome)
print('Idade: %d' %idade)
print('Salário: %.2f' %salario)
print('Sexo: %s' %sexo)
print('Estado Civel: %s' %civil)