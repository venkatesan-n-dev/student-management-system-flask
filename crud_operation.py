from db_connection import get_connection


class StudentCRUD:

    @staticmethod
    def create_student(id, name, location):
        conn = get_connection()
        cursor = conn.cursor()

        query = """
        INSERT INTO student(id, name, location)
        VALUES (?,?,?)
        """

        cursor.execute(query, (id, name, location))
        conn.commit()

        cursor.close()
        conn.close()
        return "inserted successfully"


    @staticmethod
    def get_all_students():
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM student")

        students = cursor.fetchall()

        cursor.close()
        conn.close()

        return students


    @staticmethod
    def get_student_by_id(student_id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM student WHERE id=?",
            (student_id,)
        )

        student = cursor.fetchone()

        cursor.close()
        conn.close()

        return student


    @staticmethod
    def update_student(student_id, name, location):
        conn = get_connection()
        cursor = conn.cursor()

        query = """
        UPDATE student
        SET name=?,
            location=?
        WHERE id=?
        """

        cursor.execute(query, (name, location, student_id))
        conn.commit()

        cursor.close()
        conn.close()
        return"updated successfully"


    @staticmethod
    def delete_student(student_id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM student WHERE id=?",
            (student_id,)
        )

        conn.commit()

        cursor.close()
        conn.close()
        return"deleted successfully"