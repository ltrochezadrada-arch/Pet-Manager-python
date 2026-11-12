class clsDoctor:
    
    def __init__(self, name: str, licence: str):
        self._name = name
        self._licence = licence

    @property
    def name(self) -> str:
        """Equivalente a getName()"""
        return self._name

    @name.setter
    def name(self, value: str):
        """Equivalente a setName(String name)"""
        self._name = value

    @property
    def licence(self) -> str:
        """Equivalente a getLicence()"""
        return self._licence

    @licence.setter
    def licence(self, value: str):
        """Equivalente a setLicence(String licence)"""
        self._licence = value