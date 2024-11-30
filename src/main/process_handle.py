from .constructor.process_introduction import processo_introducao

def start() -> None:
    while True:
        comando = processo_introducao()
        if comando == '1': print("Comando 1 foi acionado")
        elif comando == '2': print("Comando 2 foi acionado")
        elif comando == '5': exit()
        else: print("\n Comando não encontrado. \n\n")