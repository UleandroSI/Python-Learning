# Faça um programa que leia um nome de usuário e a sua senha e
#não aceite a senha igual ao nome do usuário, mostrando uma mensagem de
#erro e voltando a pedir as informações.

usuario = input('Digite o usuário: ')
senha = input('Digite o senha: ')

while usuario == senha:
    print('Usuario e senha não podem ser identicos, digite novamente!')
    usuario = input('Digite o usuário: ')
    senha = input('Digite o senha: ')
    
print('\nUsuário: ',usuario)
print('Senha: ',senha)