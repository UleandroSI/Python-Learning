# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# a. "Telefonou para a vítima?"
# b. "Esteve no local do crime?"
# c. "Mora perto da vítima?"
# d. "Devia para a vítima?"
# e. "Já trabalhou com a vítima?"
# O programa deve no final emitir uma classificação sobre a participação da pessoa no
# crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4
# como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

# Entrada
s = 0
print(" Responda apenas sim , ou não.")
a = input("a. Telefonou para a vítima? \n")
a = a.lower()
b = input("b. Esteve no local do crime? \n")
b = b.lower()
c = input("c. Mora perto da vítima? \n")
c = c.lower()
d = input("d. Devia para a vítima? \n")
d = d.lower()
e = input("e. Já trabalhou com a vítima? \n")
e = e.lower()

# Execuçao
if a not in "sim,não":
    print("Opção A invalida.")
    exit()
elif a == "sim":
    s += 1
if b not in "sim,não":
    print("Opção B invalida.")
    exit()
elif b == "sim":
    s += 1
if c not in "sim,não":
    print("Opção C invalida.")
    exit()
elif c == "sim":
    s += 1
if d not in "sim,não":
    print("Opção D invalida.")
    exit()
elif d == "sim":
    s += 1
if e not in "sim não":
    print("Opção E invalida.")
    exit()
elif e == "sim":
    s += 1
print("\n")
if s == 5:
    print("Assassino.")
elif s >= 3:
    print("Cumplice.")
elif s == 2:
    print("Suspeita.")
else:
    print("Inocente.")