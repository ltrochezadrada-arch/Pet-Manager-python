from Model.modelDog import ModelDog
from Model.modelCat import ModelCat

class CtlPet:
    def __init__(self):
        self.model_dog = ModelDog()  # Puente entre controlador y modelo
        self.model_cat = ModelCat()  # Puente entre controlador y modelo

    def create_pet(self, pet) -> bool:
        try:
            animal_type = pet.get_animal_type()
            if animal_type == "Dog":
                return self.model_dog.create_pet(pet)
            elif animal_type == "Cat":
                return self.model_cat.create_pet(pet)
            return False
        except Exception:
            return False

    def search_pet(self, code: str, animal_type: str):
        pet = None
        try:
            if animal_type == "Cat":
                pet = self.model_cat.search_pet(code)
            elif animal_type == "Dog":
                pet = self.model_dog.search_pet(code)
            return pet
        except Exception:
            return None

    def edit_pet(self, pet) -> bool:
        try:
            animal_type = pet.get_animal_type()
            if animal_type == "Cat":
                return self.model_cat.edit_pet(pet)
            elif animal_type == "Dog":
                return self.model_dog.edit_pet(pet)
            return False
        except Exception:
            return False

    def delete_pet(self, pet) -> bool:
        try:
            animal_type = pet.get_animal_type()
            if animal_type == "Cat":
                return self.model_cat.delete_pet(pet)
            elif animal_type == "Dog":
                return self.model_dog.delete_pet(pet)
            return False
        except Exception:
            return False

    def list_pet(self, animal_type: str) -> list:
        pet_list = None
        try:
            if animal_type == "Dog":
                pet_list = self.model_dog.list_pet()
            elif animal_type == "Cat":
                pet_list = self.model_cat.list_pet()
            return pet_list
        except Exception:
            return None

    def list_pet_by_health_status(self) -> list:
        # Cualquiera de los dos permite graficar el número de mascotas agrupadas por estado de salud
        report = self.model_cat.list_pet_by_health_status()
        return report

    def list_dog_by_health_status(self) -> list:
        report = self.model_dog.list_dog_by_health_status()
        return report

    def list_cat_by_health_status(self) -> list:
        report = self.model_cat.list_cat_by_health_status()
        return report