import mysql.connector

class StudentScoresRetriever:

    def __init__(self, host, user, password, database):

        self.host = host

        self.user = user

        self.password = password

        self.database = database


    def get_student_scores(self, student_id, student_email):

        # Create a database connection
        database = mysql.connector.connect(

            host=self.host,

            user=self.user,

            password=self.password,

            database=self.database

        )


        # Create a cursor object
        cursor = database.cursor(dictionary=True)

        # Check if the student exists in the database
        cursor.execute("SELECT * FROM STUDENT WHERE Student_ID = %s AND Student_Email = %s", (student_id, student_email))

        student = cursor.fetchone()

        if student:

            # If the student exists, retrieve their unit scores
            cursor.execute("""
                SELECT su.Course_Unit_Code AS unit, su.Result_Score AS mark
                FROM STUDENT_UNIT su
                WHERE su.Student_ID = %s
            """, (student_id,))

            scores = [{'unit': entry['unit'], 'mark': entry['mark']} for entry in cursor.fetchall()]

            return scores

        else:
            print("Student not found in the database.")

        # Close the cursor and database connection
        cursor.close()
        
        database.close()






