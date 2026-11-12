class DbData:
    def __init__(self):
        self._driver = "com.mysql.jdbc.Driver"
        self._user = "root"
        self._password = ""
        self._url = "jdbc:mysql://localhost:3306/administracionmascotasbd"

    @property
    def driver(self) -> str:
        return self._driver

    @property
    def user(self) -> str:
        return self._user

    @property
    def password(self) -> str:
        return self._password

    @property
    def url(self) -> str:
        return self._url