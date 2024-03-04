import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="alwis"
    )

# Create a cursor object
cursor = database.cursor()

# Create the database
cursor.execute("CREATE DATABASE IF NOT EXISTS testdatabase")

# Select the database
cursor.execute("USE testdatabase")


cursor.execute("""
CREATE TABLE COORDINATOR (
    Course_Coordinator_ID VARCHAR(8) PRIMARY KEY,
    Course_Coordinator_Name VARCHAR(100) NOT NULL,
    Course_Coordinator_Email VARCHAR(100) NOT NULL UNIQUE,
    Course_Coordinator_Mobile VARCHAR(20)
)
""")

cursor.execute("""
CREATE TABLE COURSE (
    Series_No INT AUTO_INCREMENT PRIMARY KEY,
    Course_Code VARCHAR(3) NOT NULL UNIQUE,
    Course_Title VARCHAR(100) NOT NULL,
    Year_Start_Offer YEAR,
    Year_End_Offer YEAR,
    Course_Coordinator_ID VARCHAR(8),
    CONSTRAINT fk_course_coordinator_id FOREIGN KEY (Course_Coordinator_ID) REFERENCES COORDINATOR(Course_Coordinator_ID)
)
""")

cursor.execute("""
CREATE TABLE STUDENT (
    Student_ID INT(8) PRIMARY KEY,
    Student_First_Name VARCHAR(50) NOT NULL,
    Student_Last_Name VARCHAR(50) NOT NULL,
    Student_Email VARCHAR(100) NOT NULL UNIQUE,
    Student_Mobile_Phone VARCHAR(20),
    Student_Course_Status VARCHAR(20),
    Course_Series_No INT,
    CONSTRAINT fk_course_series_no FOREIGN KEY (Course_Series_No) REFERENCES COURSE(Series_No)
)
""")

cursor.execute("""
CREATE TABLE UNIT (
    Course_Unit_Code VARCHAR(7) PRIMARY KEY,
    Course_Unit_Title VARCHAR(100) NOT NULL,
    Series_No INT,
    CONSTRAINT fk_series_no FOREIGN KEY (Series_No) REFERENCES COURSE(Series_No)
)
""")

cursor.execute("""
CREATE TABLE STUDENT_UNIT (
    Record_No INT AUTO_INCREMENT PRIMARY KEY,
    Student_ID INT,
    Course_Unit_Code VARCHAR(10),
    Result_Score INT,
    Result_Grade VARCHAR(2),
    Year_Attempted YEAR,
    Semester_Attempted VARCHAR(10),
    CONSTRAINT fk_student_id FOREIGN KEY (Student_ID) REFERENCES STUDENT(Student_ID),
    CONSTRAINT fk_course_unit_code FOREIGN KEY (Course_Unit_Code) REFERENCES UNIT(Course_Unit_Code)
)
""")



# Commit the changes
database.commit()

# Close the cursor and database connection
cursor.close()

database.close()