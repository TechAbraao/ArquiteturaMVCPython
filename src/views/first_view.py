def pag_introducao():
    mensagem = '''
        Sistema Cadastral:
        * Cadastrar pessoa - 1
        * Buscar pessoa por Nome - 2
        * Sair - 5
'''
    print(mensagem)
    comando = input('Comando: ')
    return comando