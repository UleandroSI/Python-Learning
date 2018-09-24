# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

# Entrada
letra = input("Digite uma letra: ")
letra = letra.lower()
# Execução
if letra not in "a,e,i,o,u":
    print("É uma consoante!")
else:
    print("É uma vogal!")