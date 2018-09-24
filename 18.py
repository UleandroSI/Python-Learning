# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em
# Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

# Entrada
cont = 0
x = 0
minuto = 60
arquivo = float(input("Qual o tamanho do arquivo: "))
link = float(input("Qual a velocidade do link: "))

# Execução
while x < arquivo:
    cont += 1
    x += minuto * link

# Saida
print("Tempo aproximado de download. Desconsiderando taxa de transferência da rede: %.f minutos" %cont)