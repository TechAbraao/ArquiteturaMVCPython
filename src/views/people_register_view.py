import os
from typing import Dict

class PeopleRegisterView:
    def registry_person_view(self) -> Dict:
        os.system('cls||clear')

        print("Cadastrar Nova Pessoa \n\n")
        name = input("Digite o nome da pessoa:")
        age = input("Digite a idade da pessoa: ")
        height = input("Digite a altura da pessoa: ")

        new_person_informations = {
            "name": name,
            "age": age,
            "height": height,
        }

        return new_person_informations
    
    def registry_person_sucess(self, message: Dict) -> None:
        os.system('cls||clear')

        sucess_message = f'''

        Usuário cadastrado com sucesso!
        Tipo: { message["type"] }
        Registros: { message["count"] }
        Infos:
            Nome: { message["attributes"]["name"] }
            Idade: { message["attributes"]["age"] }

        '''
        print(sucess_message)

    def registry_person_fail(self, error: str) -> None:
        os.system('cls||clear')

        fail_message = f'''
            Falha ao cadastrar usuário!

            Erro: { error }
        '''
        print(fail_message)   