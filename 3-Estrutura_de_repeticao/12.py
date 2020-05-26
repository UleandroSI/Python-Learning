# Desenvolva um gerador de tabuada, capaz de gerar a tabuada
# de qualquer numero inteiro entre 1 e 10. O usuario deve
# informar de qual numero ele deseja ver a tabuada.
''' Tabuada de 5:
    5 X 1 = 5
    5 X 2 = 10
    ...
    5 X 10 = 50 '''
    
while True:
    opc = input("Digite qual tabuada deseja: ")
    if opc in '1,2,3,4,5,6,7,8,9,10':
        break
    
var_esc = int(opc)

for y in range (1,11):
    print("%i X %i = %i" %(var_esc,y,(var_esc * y)))