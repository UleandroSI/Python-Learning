#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
#Variaveis
letra = input("Digite uma letra: ")
#Processamento
letra = letra.lower()
if letra not in 'aeiou':
    print("Letra consoante")
else:
    print("Letra vogal.")