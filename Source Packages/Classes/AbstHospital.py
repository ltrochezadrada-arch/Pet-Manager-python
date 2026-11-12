from abc import ABC, abstractmethod

class AbstHospital(ABC):
    
    def __init__(self, data: str = None):
        self._data = data

    @abstractmethod
    def get_patient_type(self) -> str:
        """Método abstracto equivalente a getPatientType()"""
        pass

    @abstractmethod
    def surgery(self) -> str:
        """Método abstracto equivalente a Surgery()"""
        pass

    def get_hospital_information(self) -> str:
        return f"La información es: {self.data}"

    @property
    def data(self) -> str:
        """Equivalente a getData()"""
        return self._data

    @data.setter
    def data(self, value: str):
        """Equivalente a setData(String data)"""
        self._data = value