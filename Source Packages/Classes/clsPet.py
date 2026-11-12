from abc import ABC, abstractmethod

# Simulación de las interfaces en Java usando Clases Abstractas
class IAnimal(ABC):
    @abstractmethod
    def get_animal_type(self):
        pass

class IVertebrate(ABC):
    @abstractmethod
    def get_number_of_bones(self):
        pass


class ClsPet(IAnimal, IVertebrate):
    def __init__(self, pet_id=0, code=None, name=None, born_year=0, color=None, health_status=None, veterinary=None):
        self._pet_id = pet_id
        self._code = code
        self._name = name
        self._born_year = born_year
        self._color = color
        self._health_status = health_status
        self._veterinary = veterinary

    def eat(self):
        print(f"La mascota {self._name} está comiendo.")

    def move(self):
        print(f"La mascota {self._name} está moviéndose.")

    def sound(self):
        print(f"La mascota {self._name} está realizando el sonido.")

    # Getters y Setters usando propiedades de Python
    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def born_year(self):
        return self._born_year

    @born_year.setter
    def born_year(self, value):
        self._born_year = value

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

    @property
    def health_status(self):
        return self._health_status

    @health_status.setter
    def health_status(self, value):
        self._health_status = value

    @property
    def veterinary(self):
        return self._veterinary

    @veterinary.setter
    def veterinary(self, value):
        self._veterinary = value

    @property
    def pet_id(self):
        return self._pet_id

    @pet_id.setter
    def pet_id(self, value):
        self._pet_id = value

    def get_animal_type(self):
        return "Pet"

    def get_number_of_bones(self):
        return 0