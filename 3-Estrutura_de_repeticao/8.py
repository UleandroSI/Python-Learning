# Faça um programa que leia 5 numeros e informe a soma e a media
# dos numeros.

a = soma = 0

for x in range(1,6):
    a = float(input("Digite o %x° numero: " %x))
    soma += a
    
media = soma / 5

print("A soma dos numeros foi: ", soma)
print("A media dos numeros foi: ", media)