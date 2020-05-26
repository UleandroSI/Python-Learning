# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. 
# As perguntas são:
#  a. "Telefonou para a vítima?"
#  b. "Esteve no local do crime?"
#  c. "Mora perto da vítima?"
#  d. "Devia para a vítima?"
#  e. "Já trabalhou com a vítima?"
#  O programa deve no final emitir uma classificação sobre a participação 
# da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela 
# deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 
# como "Assassino". Caso contrário, ele será classificado como "Inocente".

#VARIAVEIS
cont = 0
print("Questionario - Responda com 's' ou 'n' as perguntas:")
a = input("Telefonou para a vítima: ")
b = input("Esteve no local do crime: ")
c = input("Mora perto da vítima: ")
d = input("Devia para a vítima: ")
e = input("Já trabalhou com a vítima: ")
#PROCESSAMENTO
a = a.lower()
b = b.lower()
c = c.lower()
d = d.lower()
e = e.lower()
if a == 's':
    cont += 1
if b == 's':
    cont += 1
if c == 's':
    cont += 1
if d == 's':
    cont += 1
if e == 's':
    cont += 1

#SAIDA
if cont == 5:
    print("Assassino.")
elif cont >= 3:
    print("Cumplice.")
elif cont == 2:
    print("Suspeito.")
else:
    print("Inocente.")