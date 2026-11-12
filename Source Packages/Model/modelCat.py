import mysql.connector
from Classes.clsCat import ClsCat
from Classes.ClsReportByHealthStatus import ClsReportByHealthStatus
from Model.DbData import DbData

class ModelCat:
    def __init__(self):
        self.db_data = DbData()

    def _get_connection(self):
        # Adaptación del URL de JDBC (jdbc:mysql://host:port/db) para mysql.connector
        # Si dbData.url tiene formato jdbc:mysql://localhost:3306/administracionmascotasbd, podemos extraer o configurar directamente:
        return mysql.connector.connect(
            host="localhost",
            port=3306,
            database="administracionmascotasbd",
            user=self.db_data.user,
            password=self.db_data.password
        )

    def create_pet(self, cat: ClsCat) -> bool:
        connection = None
        try:
            connection = self._get_connection()
            cursor = connection.cursor()
            
            # Insertar en tb_pet
            query_pet = "INSERT INTO tb_pet (code, name, born_year, color, health_status) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query_pet, (cat.code, cat.name, cat.born_year, cat.color, cat.health_status))
            connection.commit()
            
            id_pet = cursor.lastrowid
            if id_pet:
                # Insertar en tb_cat
                query_cat = "INSERT INTO tb_cat (breed, id_pet) VALUES (%s, %s)"
                cursor.execute(query_cat, (cat.breed, id_pet))
                connection.commit()
                
                if cursor.rowcount > 0:
                    cursor.close()
                    connection.close()
                    return True
            
            cursor.close()
            connection.close()
            return False
        except Exception:
            if connection:
                connection.close()
            return False

    def search_pet(self, code: str) -> ClsCat:
        cat = None
        try:
            connection = self._get_connection()
            cursor = connection.cursor()
            query = "SELECT p.id, p.code, p.name, p.born_year, p.color, p.health_status, c.id AS cat_id, c.breed FROM tb_pet AS p INNER JOIN tb_cat AS c ON p.id = c.id_pet WHERE p.code = %s"
            cursor.execute(query, (code,))
            result = cursor.fetchall()
            
            for row in result:
                pet_id, pet_code, pet_name, pet_born_year, pet_color, pet_health_status, cat_id, pet_breed = row
                cat = ClsCat(cat_id=cat_id, breed=pet_breed, pet_id=pet_id, code=pet_code, name=pet_name, born_year=pet_born_year, color=pet_color, health_status=pet_health_status)
            
            cursor.close()
            connection.close()
            return cat
        except Exception:
            return cat

    def edit_pet(self, cat: ClsCat) -> bool:
        try:
            connection = self._get_connection()
            cursor = connection.cursor()
            
            query_pet = "UPDATE tb_pet SET code = %s, name = %s, born_year = %s, color = %s, health_status = %s WHERE id = %s"
            cursor.execute(query_pet, (cat.code, cat.name, cat.born_year, cat.color, cat.health_status, cat.pet_id))
            
            query_cat = "UPDATE tb_cat SET breed = %s WHERE id = %s"
            cursor.execute(query_cat, (cat.breed, cat.cat_id))
            
            connection.commit()
            rows_updated_pet = cursor.rowcount
            
            cursor.close()
            connection.close()
            return rows_updated_pet > 0
        except Exception:
            return False

    def delete_pet(self, cat: ClsCat) -> bool:
        connection = None
        try:
            connection = self._get_connection()
            connection.autocommit = False
            cursor = connection.cursor()
            
            try:
                # Eliminar primero de tb_cat y luego de tb_pet por restricciones de clave foránea
                query_cat = "DELETE FROM tb_cat WHERE id = %s"
                cursor.execute(query_cat, (cat.cat_id,))
                
                query_pet = "DELETE FROM tb_pet WHERE id = %s"
                cursor.execute(query_pet, (cat.pet_id,))
                
                connection.commit()
                cursor.close()
                connection.close()
                return True
            except Exception:
                connection.rollback()
                cursor.close()
                connection.close()
                return False
        except Exception:
            if connection:
                connection.close()
            return False

    def list_pet(self) -> list:
        cat_list = []
        try:
            connection = self._get_connection()
            cursor = connection.cursor()
            query = "SELECT p.id, p.code, p.name, p.born_year, p.color, p.health_status, c.id AS cat_id, c.breed FROM tb_pet AS p INNER JOIN tb_cat AS c ON p.id = c.id_pet"
            cursor.execute(query)
            result = cursor.fetchall()
            
            for row in result:
                pet_id, pet_code, pet_name, pet_born_year, pet_color, pet_health_status, cat_id, pet_breed = row
                cat = ClsCat(cat_id=cat_id, breed=pet_breed, pet_id=pet_id, code=pet_code, name=pet_name, born_year=pet_born_year, color=pet_color, health_status=pet_health_status)
                cat_list.append(cat)
                
            cursor.close()
            connection.close()
            return cat_list
        except Exception:
            return cat_list

    def list_pet_by_health_status(self) -> list:
        report = []
        try:
            connection = self._get_connection()
            cursor = connection.cursor()
            query = "SELECT health_status, count(health_status) FROM tb_pet GROUP BY health_status"
            cursor.execute(query)
            result = cursor.fetchall()
            
            for row in result:
                health_status_type, amount = row
                record = ClsReportByHealthStatus(health_status=health_status_type, amount_of_pets_by_health_status=amount)
                report.append(record)
                
            cursor.close()
            connection.close()
            return report
        except Exception:
            return report

    def list_cat_by_health_status(self) -> list:
        report = []
        try:
            connection = self._get_connection()
            cursor = connection.cursor()
            query = "SELECT a.health_status, count(a.health_status) FROM (SELECT p.code, p.name, p.born_year, p.color, p.health_status, c.breed FROM tb_pet AS p INNER JOIN tb_cat AS c ON p.id = c.id_pet) AS a GROUP BY a.health_status"
            cursor.execute(query)
            result = cursor.fetchall()
            
            for row in result:
                health_status_type, amount = row
                record = ClsReportByHealthStatus(health_status=health_status_type, amount_of_pets_by_health_status=amount)
                report.append(record)
                
            cursor.close()
            connection.close()
            return report
        except Exception:
            return report