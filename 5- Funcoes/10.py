# '''Jogo de Craps.''' Faça um programa de implemente um jogo de Craps. 
# O jogador lança um par de dados, obtendo um valor entre 2 e 12. 
# Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou. 
# Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" 
# e você perdeu. Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,
# este é seu "Ponto". Seu objetivo agora é continuar jogando os dados até 
# tirar este número novamente. Você perde, no entanto, se tirar um 7 antes 
# de tirar este Ponto novamente.

# VARIAVEIS
import random
numero = 0
def dados():
    numero = random.randint(2,12)
    return numero
# PROCESSAMENTO
while True:
    numero = dados()
    if numero == 7 or numero == 11:
        print("Voce e um natural \nVenceu com: %d" %numero)
        break
    elif numero == 2 or numero == 3 or numero == 12:
        print("Voce e um craps \nPerdeu com: %d" %numero)
        break
    else:
        while True:
            ponto = numero
            numero = dados()
            #print("Ponto: ",ponto) Prova Real
            #print(numero) Prova Real
            if numero == ponto:
                print("Voce Venceu com: %d" %numero)
                break
            elif numero == 7:
                print("Voce Perdeu pelo 7.")
                break
            else:
                numero = ponto
        break