from .constructor.process_introduction import processo_introducao
from .constructor.people_finder_constructor import people_finder_constructor
from .constructor.people_register_constructor import people_register_constructor


def start() -> None:
    while True:
        comando = processo_introducao()
        if comando == '1': people_register_constructor()
        elif comando == '2': people_finder_constructor()
        elif comando == '5': exit()
        else: print("\n Comando não encontrado. \n\n")