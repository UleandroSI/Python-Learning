# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino,
# Sexo Inválido.

# Entrada
letra = input("Digite somente as letras 'F' para Feminino ou 'M' para masculino: ")
letra = letra.lower()

# Execução
if letra not in "f,m":
    print("Sexo Inválido!")
elif letra == "f":
    print("Sexo Feminino!")
else:
    print("Sexo Masculino!")