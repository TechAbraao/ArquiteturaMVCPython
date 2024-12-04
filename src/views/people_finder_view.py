from typing import Dict
import os

class PeopleFinderView:
    def find_person_view(self) -> Dict: 
        os.system('cls||clear')

        print("Buscar Pessoa \n\n")
        name = input("Determine o nome da pessoa para a a busca:")

        person_finder_informations = {
            "name": name
        }

        return person_finder_informations
    
    def find_person_sucess(self, message: Dict) -> None:
        os.system('cls||clear')

        sucess_message = f''''
            Usuário encontrado com sucesso!

            Tipo: { message["type"] }
            Registros: { message["count"] }
            Infos:
                Name: { message["infos"]["name"] }
        '''
        print(sucess_message)

    def find_person_fail(self, error: str) -> None:
        os.system('cls||clear')

        fail_message = f''''
            Falha ao encontrar o usuário!

            Erro: { error }

        '''

        print(fail_message)