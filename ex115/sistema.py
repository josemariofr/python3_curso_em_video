from biblioteca.interf import *
from biblioteca.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)   
    
while True:
    resp = menu(['Novo Arquivo', 'Cadastro', 'Listar Usuários', 'Sair'])
    if resp == 1:
        cabeçalho('Opção 1')
    elif resp == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resp == 3:
        lerArquivo(arq)
    elif resp == 4:
        cabeçalho('Saindo...')
        sleep(2)
        break
    else:
        print('\033[33mERRO! DIGITE UMA OPÇÃO VÁLIDA\033[m')