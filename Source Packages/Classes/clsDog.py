from Classes.clsPet import ClsPet


class ClsDog(ClsPet):
    def __init__(self, dog_id=0, breed=None, pedigree=False, pet_id=0, code=None, name=None, born_year=0, color=None, health_status=None):
        super().__init__(pet_id, code, name, born_year, color, health_status)
        self._dog_id = dog_id
        self._breed = breed
        self._pedigree = pedigree

    # Simulación de sobrecarga para WalkAround en Java
    def walk_around(self, param=None):
        if param is None:
            print(f"El perro {self.get_name()} esta caminando.")
        elif isinstance(param, int):
            print(f"El perro {self.get_name()} esta caminando {param} km")
        elif isinstance(param, bool):
            has_leash = "con correa" if param else "sin correa"
            print(f"El perro {self.get_name()} esta caminando {has_leash}")

    def sound(self):
        print(f"El perro {self.get_name()} hace Guuuuaaaauuu")

    def get_animal_type(self):
        return "Dog"

    def get_number_of_bones(self):
        return 320

    # Getters y Setters usando propiedades de Python
    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, value):
        self._breed = value

    @property
    def pedigree(self):
        return self._pedigree

    @pedigree.setter
    def pedigree(self, value):
        self._pedigree = value

    @property
    def dog_id(self):
        return self._dog_id

    @dog_id.setter
    def dog_id(self, value):
        self._dog_id = value