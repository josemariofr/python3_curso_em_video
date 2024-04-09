from biblioteca.interf import *
from time import sleep

while True:
    resp = menu(['Novo Arquivo', 'Cadastro', 'Listar Usuários', 'Sair'])
    if resp == 1:
        cabeçalho ('Opção 1')
    elif resp == 2:
        cabeçalho('Opção 2')
    elif resp == 3:
        cabeçalho('Opção 3')
    elif resp == 4:
        cabeçalho('Saindo...')
        sleep(2)
        break
    else:
        print('\033[33mERRO! DIGITE UMA OPÇÃO VÁLIDA\033[m')