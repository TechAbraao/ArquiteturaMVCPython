from typing import Dict

class PeopleFinderController:
    def find_by_name(self, person_finder_informations: Dict) -> Dict:
        try:
            self.__validate_fields(person_finder_informations)
            # person = Buscar em Banco de Dados
            response = self.__format__response(None)
            return { "sucess": True, "message": response }
        except Exception as exception:
            return { "sucess": False, "error": str(exception) }

    def __validate_fields(self, person_finder_informations: Dict) -> Dict:
        if not isinstance(person_finder_informations["name"], str):
            raise Exception("Campo nome inválido!")
        
    def __format__response(self, person: any) -> Dict:
        return {
            "count": 1,
            "type": "Person",
            "infos": {
                "name": "Abraão"
            }
        }