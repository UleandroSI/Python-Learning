# Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo,
# o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. Deve haver pelo menos duas funções:
# uma para fazer a conversão e uma para a saída. Registre a informação A.M./P.M. como um valor ‘A’ para A.M.
# e ‘P’ para P.M. Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M.
# ou P.M. Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada
# todas as vezes que desejar.

def converter(hora):
    global periodo
    if hora > 12:
        periodo = 'P'
        if hora == 13:
            return 1
        elif hora == 14:
            return 2
        elif hora == 15:
            return 3
        elif hora == 16:
            return 4
        elif hora == 17:
            return 5
        elif hora == 18:
            return 6
        elif hora == 19:
            return 7
        elif hora == 20:
            return 8
        elif hora == 21:
            return 9
        elif hora == 22:
            return 10
        elif hora == 23:
            return 11
        elif hora == 24:
            return 12
    else:
        periodo = 'A'
        return hora

def saida(hora,minutos,h):
    if hora <= 12:
        print("Convertido: %d:%d %s" %(hora,minutos,periodo))
    else:
        print("Convertido: %d:%d %s" %(h,minutos,periodo))

while True:
    hora = int(input("Digite a hora: "))
    if hora < 1 or hora > 24:
        print("Hora invalida.\n Digite novamente.")
    else:
        minutos = int(input("Digite os minutos: "))
        if minutos < 0 or minutos > 59:
            print("Minutos invalidos\n Recomece novamente.")
        else:
            h = converter(hora)
            saida(hora,minutos,h)
    op = input("Digite S para Sair: ")
    op = op.lower()
    if op == 's':
        break