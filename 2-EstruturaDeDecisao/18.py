# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine 
# se a mesma é uma data válida.

#VARIAVEIS
dia = mes = ano = int
data = input("Digite uma data no formato 'dd/mm/aaaa': ")

#PROCESSAMENTO
if len(data) != 10:
    print("Data invalida.")
elif data[2] != '/' or data[5] != '/':
    print("Data invalida.")
else:
    dia = int(data[0:2])
    mes = int(data[3:5])
    ano = int(data[6:])
    if ano < 0:
        print("Data invalida.")
    else:
        if dia < 0 or dia > 31:
            print("Data invalida.")
        else:
            if mes < 0 or mes > 12:
                print("Data invalida.")
            else:
                if mes == 2:
                    if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0:
                        if dia > 29:
                            print("Data invalida.")
                        else:
                            print("Data valida")
                    else:
                        if dia > 28:
                            print("Data invalida.")
                        else:
                            print("Data valida")
                elif mes == 4:
                    if dia > 30:
                        print("Data invalida.")
                    else:
                        print("Data valida")
                elif mes == 6:
                    if dia > 30:
                        print("Data invalida.")
                    else:
                        print("Data valida")
                elif mes == 9:
                    if dia > 30:
                        print("Data invalida.")
                    else:
                        print("Data valida")
                elif mes == 11:
                    if dia > 30:
                        print("Data invalida.")
                    else:
                        print("Data valida")