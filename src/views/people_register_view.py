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