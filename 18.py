# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

# Definindo função
def validarAno():
    # Se for bissexto retorna TRUE
    global aa
    if aa % 400 == 0:
        volta = True
    else:
        if aa % 4 == 0 and aa % 100 != 0:
            volta = True
        else:
            volta = False
    return volta
# Entrada
data = input("Digite a data em formato 'dd/mm/aaaa : ")

# Execuçao
if len(data) != 10:
    print("Data invalida.")
else:
    if data[0:2].isnumeric() and data[3:5].isnumeric() and data[6:11].isnumeric():
        if data[2] != '/' or data[5] != '/':
            print("Data inválida.")
        else:
            dd = int(data[0:2])
            mm = int(data[3:5])
            aa = int(data[6:10])
            if mm < 1 or mm > 12:
                print("Data invalida.")
            elif mm==1 or mm==3 or mm==5 or mm==7 or mm==8 or mm==10 or mm==12:
                if dd < 1 or dd > 31:
                    print("Data invalida.")
                else:
                    print("Data valida.")
            elif mm==4 or mm==6 or mm==9 or mm==11:
                if dd < 1 or dd > 30:
                    print("Data invalida.")
                else:
                    print("Data valida.")
            else:
                bissexto = validarAno()
                if bissexto == True:
                    if dd < 1 or dd > 29:
                        print("Data invalida")
                    else:
                        print("Data valida.")
                else:
                    if dd < 1 or dd > 28:
                        print("Data invalida")
                    else:
                        print("Data valida.")
    else:
        print("Data invalida.")