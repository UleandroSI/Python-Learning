# Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
#Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

#Variaveis
letra = input("Digite a opçao: ")
#Processamento
letra = letra.lower()
if letra == 'f':
    print("F - Feminino.")
elif letra == 'm':
    print("M - Masculino.")
else:
    print("Sexo invalido.")
#Saida