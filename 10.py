# Faça um programa que pergunte em que turno você estuda. Peça para digitar M-Matutino, V-Vespertino, e N-Noturno.
# Imprima a mensagem "Bom dia!", "Boa tarde!", "Boa noite!", "Ou valor invalido!". conforme o caso.

# Entrada
turno = input("Digite M para Matutino, V -Vespertino ou N -Noturno: ")

# Saida
turno = turno.lower()
if turno not in "m,n,v":
    print("Valor inválido!")
elif turno == "m":
    print("Bom dia!")
elif turno == "v":
    print("Bom tarde!")
else:
    print("Boa noite!")