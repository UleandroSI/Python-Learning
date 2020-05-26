# Faça um programa que peça o tamanho de um arquivo para download (em MB) 
#e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo 
#aproximado de download do arquivo usando este link (em minutos).

# Variaveis
arquivo = float(input("Digite o tamanho do arquivo em MB: "))
link = float(input("Digite a velocidade do link em Mbps: "))
# Processamento
taxa = link/ 8
tempo = arquivo / taxa
minutos = tempo / 60
# Saida
print("Tempo aproximado de download em minutos: %.1f" %minutos)