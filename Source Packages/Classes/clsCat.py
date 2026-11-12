from Classes.clsPet import ClsPet


class ClsCat(ClsPet):
    def __init__(self, cat_id=0, breed=None, pet_id=0, code=None, name=None, born_year=0, color=None, health_status=None):
        super().__init__(pet_id, code, name, born_year, color, health_status)
        self._cat_id = cat_id
        self._breed = breed

    # Getter y Setter para catId
    @property
    def cat_id(self):
        return self._cat_id

    @cat_id.setter
    def cat_id(self, value):
        self._cat_id = value

    # Getter y Setter para breed
    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, value):
        self._breed = value

    def self_cleaning(self):
        print(f"El gato {self.get_name()} se está limpiando.")

    def sound(self):
        print(f"El gato {self.get_name()} hace miaaauuu")

    def get_number_of_bones(self):
        return 230

    def get_animal_type(self):
        return "Cat"