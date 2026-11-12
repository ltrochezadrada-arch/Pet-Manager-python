from abc import ABC, abstractmethod

# Simulación de la clase abstracta AbstHospital en Java
class AbstHospital(ABC):
    @abstractmethod
    def get_patient_type(self):
        pass

    @abstractmethod
    def surgery(self):
        pass


class ClsVeterinary(AbstHospital):
    def __init__(self, name=None, phone=None, address=None, doctor=None):
        self._name = name
        self._phone = phone
        self._address = address
        self._doctor = doctor

    def pet_care(self, pet):
        print(f"Atendiendo a la mascota {pet.name}")
        return pet.health_status

    # Getters y Setters usando propiedades de Python
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value

    @property
    def doctor(self):
        return self._doctor

    @doctor.setter
    def doctor(self, value):
        self._doctor = value

    def get_patient_type(self):
        return "Animal"

    def surgery(self):
        return "Surgery animal data"