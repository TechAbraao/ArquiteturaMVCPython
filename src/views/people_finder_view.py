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