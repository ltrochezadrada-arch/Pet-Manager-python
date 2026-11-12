class ClsReportByHealthStatus:
    def __init__(self, health_status=None, amount_of_pets_by_health_status=0):
        self._health_status = health_status
        self._amount_of_pets_by_health_status = amount_of_pets_by_health_status

    @property
    def health_status(self):
        return self._health_status

    @health_status.setter
    def health_status(self, value):
        self._health_status = value

    @property
    def amount_of_pets_by_health_status(self):
        return self._amount_of_pets_by_health_status

    @amount_of_pets_by_health_status.setter
    def amount_of_pets_by_health_status(self, value):
        self._amount_of_pets_by_health_status = value