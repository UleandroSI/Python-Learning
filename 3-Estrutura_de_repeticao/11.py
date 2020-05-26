# Altere o programa anterior para no final mostrar a soma dos numeros
soma = 0
num1 = int(input("Digite o menor numero: "))
num2 = int(input("Digite o maior numero: "))
    
for y in range(num1+1,num2):
    soma = soma + y
    print(y)

print("Soma igual: ",soma)