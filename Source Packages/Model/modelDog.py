import mysql.connector
from Classes.clsDog import ClsDog
from Classes.ClsReportByHealthStatus import ClsReportByHealthStatus
from Model.DbData import DbData

class ModelDog:
    def __init__(self):
        self.db_data = DbData()

    def _get_connection(self):
        return mysql.connector.connect(
            host="localhost",
            port=3306,
            database="administracionmascotasbd",
            user=self.db_data.user,
            password=self.db_data.password
        )

    def create_pet(self, dog: ClsDog) -> bool:
        connection = None
        try:
            connection = self._get_connection()
            cursor = connection.cursor()
            
            # Insertar en tb_pet
            query_pet = "INSERT INTO tb_pet (code, name, born_year, color, health_status) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query_pet, (dog.code, dog.name, dog.born_year, dog.color, dog.health_status))
            connection.commit()
            
            id_pet = cursor.lastrowid
            if id_pet:
                # Insertar en tb_dog
                query_dog = "INSERT INTO tb_dog (breed, pedigree, id_pet) VALUES (%s, %s, %s)"
                cursor.execute(query_dog, (dog.breed, dog.pedigree, id_pet))
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

    def search_pet(self, code: str) -> ClsDog:
        dog = None
        try:
            connection = self._get_connection()
            cursor = connection.cursor()
            query = "SELECT p.id, p.code, p.name, p.born_year, p.color, p.health_status, d.id AS dog_id, d.breed, d.pedigree FROM tb_pet AS p INNER JOIN tb_dog AS d ON p.id = d.id_pet WHERE p.code = %s"
            cursor.execute(query, (code,))
            result = cursor.fetchall()
            
            for row in result:
                pet_id, pet_code, pet_name, pet_born_year, pet_color, pet_health_status, dog_id, pet_breed, pet_pedigree = row
                dog = ClsDog(dog_id=dog_id, breed=pet_breed, pedigree=pet_pedigree, pet_id=pet_id, code=pet_code, name=pet_name, born_year=pet_born_year, color=pet_color, health_status=pet_health_status)
            
            cursor.close()
            connection.close()
            return dog
        except Exception:
            return dog

    def edit_pet(self, dog: ClsDog) -> bool:
        try:
            connection = self._get_connection()
            cursor = connection.cursor()
            
            query_pet = "UPDATE tb_pet SET code = %s, name = %s, born_year = %s, color = %s, health_status = %s WHERE id = %s"
            cursor.execute(query_pet, (dog.code, dog.name, dog.born_year, dog.color, dog.health_status, dog.pet_id))
            
            query_dog = "UPDATE tb_dog SET breed = %s, pedigree = %s WHERE id = %s"
            cursor.execute(query_dog, (dog.breed, dog.pedigree, dog.dog_id))
            
            connection.commit()
            rows_updated_pet = cursor.rowcount
            
            cursor.close()
            connection.close()
            return rows_updated_pet > 0
        except Exception:
            return False

    def delete_pet(self, dog: ClsDog) -> bool:
        connection = None
        try:
            connection = self._get_connection()
            connection.autocommit = False
            cursor = connection.cursor()
            
            try:
                # Eliminar primero de la tabla específica (tb_dog) y luego de la general (tb_pet)
                query_dog = "DELETE FROM tb_dog WHERE id = %s"
                cursor.execute(query_dog, (dog.dog_id,))
                
                query_pet = "DELETE FROM tb_pet WHERE id = %s"
                cursor.execute(query_pet, (dog.pet_id,))
                
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
        dog_list = []
        try:
            connection = self._get_connection()
            cursor = connection.cursor()
            query = "SELECT p.id, p.code, p.name, p.born_year, p.color, p.health_status, d.id AS dog_id, d.breed, d.pedigree FROM tb_pet AS p INNER JOIN tb_dog AS d ON p.id = d.id_pet"
            cursor.execute(query)
            result = cursor.fetchall()
            
            for row in result:
                pet_id, pet_code, pet_name, pet_born_year, pet_color, pet_health_status, dog_id, pet_breed, pet_pedigree = row
                dog = ClsDog(dog_id=dog_id, breed=pet_breed, pedigree=pet_pedigree, pet_id=pet_id, code=pet_code, name=pet_name, born_year=pet_born_year, color=pet_color, health_status=pet_health_status)
                dog_list.append(dog)
                
            cursor.close()
            connection.close()
            return dog_list
        except Exception:
            return dog_list

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

    def list_dog_by_health_status(self) -> list:
        report = []
        try:
            connection = self._get_connection()
            cursor = connection.cursor()
            query = "SELECT a.health_status, count(a.health_status) FROM (SELECT p.code, p.name, p.born_year, p.color, p.health_status, d.breed, d.pedigree FROM tb_pet AS p INNER JOIN tb_dog AS d ON p.id = d.id_pet) AS a GROUP BY a.health_status"
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