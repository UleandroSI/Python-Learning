# '''Embaralha palavra'''. Construa uma função que receba uma string como 
# parâmetro e devolva outra string com os carateres embaralhados. 
# Por exemplo: se função receber a palavra ''python'', pode retornar ''npthyo'',
# ''ophtyn'' ou qualquer outra combinação possível, de forma aleatória. 
# Padronize em sua função que todos os caracteres serão devolvidos em caixa 
# alta ou caixa baixa, independentemente de como foram digitados.

# VARIAVEIS
def embaralha(palavra):
    import random
    lista = list(palavra)
    random.shuffle(lista)
    return ''.join(lista)

# PROCESSAMENTO
palavra = input("Digite uma palavra: ")
palavra = palavra.lower()
retorno = embaralha(palavra)

# SAIDA
print(retorno)