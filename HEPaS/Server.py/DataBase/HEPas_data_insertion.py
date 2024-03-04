import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="alwis",
    database="testdatabase"  # Include the database name
)

# Create a cursor object
cursor = database.cursor()

# Insert data into COORDINATOR table for multiple courses
cursor.execute("""
INSERT INTO COORDINATOR (Course_Coordinator_ID, Course_Coordinator_Name, Course_Coordinator_Email, Course_Coordinator_Mobile)
VALUES 
    ('IT123456', 'John Doe', 'JohnDoe@my.oust.edu.au', '+61 412 123 678'),
    ('CS789012', 'Jane Smith', 'JaneSmith@my.oust.edu.au', '+61 434 456 901'),
    ('DS345678', 'David Johnson', 'DavidJohnson@my.oust.edu.au', '+61 456 789 234'),
    ('PH234567', 'Sarah Brown', 'SarahBrown@my.oust.edu.au', '+61 478 012 567'),
    ('TE456789', 'Michael White', 'MichaelWhite@my.oust.edu.au', '+61 490 345 890')
""")

# Insert data into COURSE table
cursor.execute("""
INSERT INTO COURSE (Course_Code, Course_Title, Year_Start_Offer, Year_End_Offer, Course_Coordinator_ID)
VALUES 
    ('IT', 'Information Technology', 1998, NULL, 'IT123456'),
    ('CS', 'Cyber Security', 2000, NULL, 'CS789012'),
    ('DS', 'Data Science', 2005, NULL, 'DS345678'),
    ('PH', 'Physics', 2000, NULL, 'PH234567'),
    ('TE', 'Tertiary Education', 2000, 2020, 'TE456789')
""")


# Insert data into STUDENT table with updated Student_ID and Student_Email format
cursor.execute("""
INSERT INTO STUDENT (Student_ID, Student_First_Name, Student_Last_Name, Student_Email, Student_Mobile_Phone, Student_Course_Status, Course_Series_No)
VALUES 
    (10000001, 'Alice', 'Smith', 'alice.smith@student.oust.edu.au', '+61 400 111 222', 'completed', 1),
    (10000002, 'Bob', 'Johnson', 'bob.johnson@student.oust.edu.au', '+61 411 222 333', 'completed', 2),
    (10000003, 'Charlie', 'Williams', 'charlie.williams@student.oust.edu.au', '+61 422 333 444', 'completed', 3),
    (10000004, 'David', 'Brown', 'david.brown@student.oust.edu.au', '+61 433 444 555', 'completed', 4),
    (10000005, 'Eva', 'Jones', 'eva.jones@student.oust.edu.au', '+61 444 555 666', 'in progess', 5),
    (10000006, 'Frank', 'Davis', 'frank.davis@student.oust.edu.au', '+61 455 666 777', 'completed', 1),
    (10000007, 'Grace', 'Miller', 'grace.miller@student.oust.edu.au', '+61 466 777 888', 'in progess', 2),
    (10000008, 'Harry', 'Taylor', 'harry.taylor@student.oust.edu.au', '+61 477 888 999', 'completed', 3)
""")

# Insert data into UNIT table for Information Technology
cursor.execute("""
INSERT INTO UNIT (Course_Unit_Code, Course_Unit_Title, Series_No)
VALUES 
    ('IT23034', 'Programming Fundamentals', 1),
    ('IT23035', 'Database Management', 1),
    ('IT23036', 'Web Development', 1),
    ('IT23037', 'Network Security', 1),
    ('IT23038', 'Software Engineering', 1),
    ('IT23039', 'Data Structures', 1),
    ('IT23040', 'Artificial Intelligence', 1),
    ('IT23041', 'Cybersecurity Fundamentals', 1),
    ('IT23042', 'Mobile App Development', 1),
    ('IT23043', 'Cloud Computing', 1),
    ('IT23044', 'Computer Networks', 1),
    ('IT23045', 'Human-Computer Interaction', 1),
    ('IT23046', 'Machine Learning', 1),
    ('IT23047', 'Information Systems', 1),
    ('IT23048', 'Distributed Systems', 1),
    ('IT23049', 'Computer Graphics', 1)
""")

# Insert data into UNIT table for Cyber Security
cursor.execute("""
INSERT INTO UNIT (Course_Unit_Code, Course_Unit_Title, Series_No)
VALUES 
    ('CS23034', 'Network Security', 2),
    ('CS23035', 'Ethical Hacking', 2),
    ('CS23036', 'Incident Response', 2),
    ('CS23037', 'Cryptography', 2),
    ('CS23038', 'Security Governance', 2),
    ('CS23039', 'Penetration Testing', 2),
    ('CS23040', 'Digital Forensics', 2),
    ('CS23041', 'Security Policies and Procedures', 2),
    ('CS23042', 'Malware Analysis', 2),
    ('CS23043', 'Wireless Security', 2),
    ('CS23044', 'Security Awareness Training', 2),
    ('CS23045', 'Cybersecurity Risk Management', 2),
    ('CS23046', 'Cloud Security', 2),
    ('CS23047', 'IoT Security', 2),
    ('CS23048', 'Blockchain Security', 2),
    ('CS23049', 'Mobile Security', 2)
""")

# Insert data into UNIT table for Data Science
cursor.execute("""
INSERT INTO UNIT (Course_Unit_Code, Course_Unit_Title, Series_No)
VALUES 
    ('DS23034', 'Introduction to Data Science', 3),
    ('DS23035', 'Data Mining', 3),
    ('DS23036', 'Machine Learning Algorithms', 3),
    ('DS23037', 'Big Data Analytics', 3),
    ('DS23038', 'Statistical Analysis', 3),
    ('DS23039', 'Data Visualization', 3),
    ('DS23040', 'Natural Language Processing', 3),
    ('DS23041', 'Deep Learning', 3),
    ('DS23042', 'Time Series Analysis', 3),
    ('DS23043', 'Data Ethics', 3),
    ('DS23044', 'Advanced Topics in Data Science', 3),
    ('DS23045', 'Data Science Project', 3),
    ('DS23046', 'Data Warehousing', 3),
    ('DS23047', 'Text Analytics', 3),
    ('DS23048', 'Spatial Data Science', 3),
    ('DS23049', 'Data Science for Business', 3)
""")

# Insert data into UNIT table for Physics
cursor.execute("""
INSERT INTO UNIT (Course_Unit_Code, Course_Unit_Title, Series_No)
VALUES 
    ('PH23034', 'Classical Mechanics', 4),
    ('PH23035', 'Quantum Mechanics', 4),
    ('PH23036', 'Electromagnetism', 4),
    ('PH23037', 'Thermodynamics', 4),
    ('PH23038', 'Optics', 4),
    ('PH23039', 'Modern Physics', 4),
    ('PH23040', 'Statistical Mechanics', 4),
    ('PH23041', 'Nuclear Physics', 4),
    ('PH23042', 'Astrophysics', 4),
    ('PH23043', 'Condensed Matter Physics', 4),
    ('PH23044', 'Particle Physics', 4),
    ('PH23045', 'Plasma Physics', 4),
    ('PH23046', 'Quantum Field Theory', 4),
    ('PH23047', 'Cosmology', 4),
    ('PH23048', 'Biophysics', 4),
    ('PH23049', 'Experimental Physics', 4)
""")

# Insert data into UNIT table for Tertiary Education
cursor.execute("""
INSERT INTO UNIT (Course_Unit_Code, Course_Unit_Title, Series_No)
VALUES 
    ('TE23034', 'Teaching Methods', 5),
    ('TE23035', 'Assessment and Evaluation', 5),
    ('TE23036', 'Educational Psychology', 5),
    ('TE23037', 'Curriculum Development', 5),
    ('TE23038', 'Technology in Education', 5),
    ('TE23039', 'Inclusive Education', 5),
    ('TE23040', 'Educational Leadership', 5),
    ('TE23041', 'Higher Education Policy', 5),
    ('TE23042', 'Student Development', 5),
    ('TE23043', 'Global Education', 5),
    ('TE23044', 'Research in Education', 5),
    ('TE23045', 'Adult Learning', 5),
    ('TE23046', 'Special Education', 5),
    ('TE23047', 'Language and Literacy in Education', 5),
    ('TE23048', 'Counseling in Education', 5),
    ('TE23049', 'Internship in Teaching', 5)
""")



# Insert data into STUDENT_UNIT table for student with ID 10000001
cursor.execute("""
INSERT INTO STUDENT_UNIT (Student_ID, Course_Unit_Code, Result_Score, Result_Grade, Year_Attempted, Semester_Attempted)
VALUES 
    (10000001, 'IT23034', 85, 'HD', 2020, 'Semester 1'),
    (10000001, 'IT23035', 75, 'D', 2020, 'Semester 1'),
    (10000001, 'IT23036', 92, 'HD', 2020, 'Semester 2'),
    (10000001, 'IT23037', 40, 'F', 2020, 'Semester 2'), 
    (10000001, 'IT23038', 40, 'F', 2021, 'Semester 1'),
    (10000001, 'IT23039', 78, 'D', 2021, 'Semester 1'),
    (10000001, 'IT23037', 72, 'D', 2021, 'Semester 2'),
    (10000001, 'IT23040', 95, 'HD', 2021, 'Semester 2'),
    (10000001, 'IT23041', 55, 'P', 2021, 'Semester 2'),
    (10000001, 'IT23038', 60, 'CR', 2022, 'Semester 1'),
    (10000001, 'IT23042', 80, 'D', 2022, 'Semester 1'),
    (10000001, 'IT23043', 72, 'CR', 2022, 'Semester 1'),
    (10000001, 'IT23044', 65, 'CR', 2022, 'Semester 2'),
    (10000001, 'IT23045', 88, 'HD', 2022, 'Semester 2'),
    (10000001, 'IT23046', 93, 'HD', 2023, 'Semester 1'),
    (10000001, 'IT23047', 47, 'F', 2023, 'Semester 1'),
    (10000001, 'IT23048', 70, 'D', 2023, 'Semester 2'),
    (10000001, 'IT23049', 82, 'HD', 2023, 'Semester 2'),
    (10000001, 'IT23047', 67, 'CR', 2024, 'Semester 1')
""")

# Insert more data for student with ID 10000002
cursor.execute("""
-- Insert data for student with ID 10000002
INSERT INTO STUDENT_UNIT (Student_ID, Course_Unit_Code, Result_Score, Result_Grade, Year_Attempted, Semester_Attempted)
VALUES 
    (10000002, 'CS23034', 78, 'D', 2020, 'Semester 1'),
    (10000002, 'CS23035', 60, 'CR', 2020, 'Semester 1'),
    (10000002, 'CS23036', 85, 'HD', 2020, 'Semester 2'),
    (10000002, 'CS23037', 40, 'F', 2020, 'Semester 2'), 
    (10000002, 'CS23038', 40, 'F', 2021, 'Semester 1'),
    (10000002, 'CS23039', 78, 'D', 2021, 'Semester 1'),
    (10000002, 'CS23037', 72, 'D', 2021, 'Semester 2'),
    (10000002, 'CS23040', 95, 'HD', 2021, 'Semester 2'),
    (10000002, 'CS23041', 55, 'P', 2021, 'Semester 2'),
    (10000002, 'CS23038', 60, 'CR', 2022, 'Semester 1'),
    (10000002, 'CS23042', 80, 'D', 2022, 'Semester 1'),
    (10000002, 'CS23043', 72, 'CR', 2022, 'Semester 1'),
    (10000002, 'CS23044', 65, 'CR', 2022, 'Semester 2'),
    (10000002, 'CS23045', 88, 'HD', 2022, 'Semester 2'),
    (10000002, 'CS23046', 93, 'HD', 2023, 'Semester 1'),
    (10000002, 'CS23047', 47, 'F', 2023, 'Semester 1'),
    (10000002, 'CS23048', 70, 'D', 2023, 'Semester 2'),
    (10000002, 'CS23049', 82, 'HD', 2023, 'Semester 2')
""")
    
# Insert more data for student with ID 10000003
cursor.execute("""
-- Insert data for student with ID 10000003
INSERT INTO STUDENT_UNIT (Student_ID, Course_Unit_Code, Result_Score, Result_Grade, Year_Attempted, Semester_Attempted)
VALUES 
    (10000003, 'DS23034', 92, 'HD', 2020, 'Semester 1'),
    (10000003, 'DS23035', 75, 'D', 2020, 'Semester 1'),
    (10000003, 'DS23036', 68, 'CR', 2020, 'Semester 2'),
    (10000003, 'DS23037', 38, 'F', 2020, 'Semester 2'), 
    (10000003, 'DS23038', 48, 'F', 2021, 'Semester 1'),
    (10000003, 'DS23039', 78, 'D', 2021, 'Semester 1'),
    (10000003, 'DS23037', 72, 'D', 2021, 'Semester 2'),
    (10000003, 'DS23040', 95, 'HD', 2021, 'Semester 2'),
    (10000003, 'DS23041', 65, 'CR', 2021, 'Semester 2'),
    (10000003, 'DS23038', 70, 'D', 2022, 'Semester 1'),
    (10000003, 'DS23042', 82, 'HD', 2022, 'Semester 1'),
    (10000003, 'DS23043', 77, 'CR', 2022, 'Semester 1'),
    (10000003, 'DS23044', 60, 'P', 2022, 'Semester 2'),
    (10000003, 'DS23045', 85, 'HD', 2022, 'Semester 2'),
    (10000003, 'DS23046', 90, 'HD', 2023, 'Semester 1'),
    (10000003, 'DS23047', 55, 'P', 2023, 'Semester 1'),
    (10000003, 'DS23048', 75, 'D', 2023, 'Semester 2'),
    (10000003, 'DS23049', 78, 'D', 2023, 'Semester 2')
""")

# Insert more data for student with ID 10000004
cursor.execute("""
-- Insert data for student with ID 10000004
INSERT INTO STUDENT_UNIT (Student_ID, Course_Unit_Code, Result_Score, Result_Grade, Year_Attempted, Semester_Attempted)
VALUES 
    (10000004, 'PH23034', 50, 'P', 2020, 'Semester 1'),
    (10000004, 'PH23035', 78, 'D', 2020, 'Semester 1'),
    (10000004, 'PH23036', 90, 'HD', 2020, 'Semester 2'),
    (10000004, 'PH23037', 34, 'F', 2020, 'Semester 2'), 
    (10000004, 'PH23038', 40, 'CR', 2021, 'Semester 1'),
    (10000004, 'PH23039', 78, 'D', 2021, 'Semester 1'),
    (10000004, 'PH23037', 72, 'D', 2021, 'Semester 2'),
    (10000004, 'PH23040', 95, 'HD', 2021, 'Semester 2'),
    (10000004, 'PH23041', 65, 'CR', 2021, 'Semester 2'),
    (10000004, 'PH23038', 70, 'D', 2022, 'Semester 1'),
    (10000004, 'PH23042', 82, 'HD', 2022, 'Semester 1'),
    (10000004, 'PH23043', 77, 'CR', 2022, 'Semester 1'),
    (10000004, 'PH23044', 60, 'P', 2022, 'Semester 2'),
    (10000004, 'PH23045', 85, 'HD', 2022, 'Semester 2'),
    (10000004, 'PH23046', 90, 'HD', 2023, 'Semester 1'),
    (10000004, 'PH23047', 55, 'P', 2023, 'Semester 1'),
    (10000004, 'PH23048', 75, 'D', 2023, 'Semester 2'),
    (10000004, 'PH23049', 78, 'D', 2023, 'Semester 2')
""")


# Insert more data for student with ID 10000005
cursor.execute("""
-- Insert data for student with ID 10000005
INSERT INTO STUDENT_UNIT (Student_ID, Course_Unit_Code, Result_Score, Result_Grade, Year_Attempted, Semester_Attempted)
VALUES 
    (10000005, 'TE23034', 40, 'F', 2020, 'Semester 1'),
    (10000005, 'TE23035', 55, 'P', 2020, 'Semester 1'),
    (10000005, 'TE23036', 68, 'CR', 2020, 'Semester 2'),
    (10000005, 'TE23037', 23, 'F', 2020, 'Semester 2'),
    (10000005, 'TE23034', 70, 'D', 2021, 'Semester 1'), 
    (10000005, 'TE23038', 40, 'F', 2021, 'Semester 1'),
    (10000005, 'TE23039', 78, 'D', 2021, 'Semester 1'),
    (10000005, 'TE23037', 82, 'HD', 2021, 'Semester 2'),
    (10000005, 'TE23040', 95, 'HD', 2021, 'Semester 2'),
    (10000005, 'TE23041', 65, 'CR', 2021, 'Semester 2'),
    (10000005, 'TE23038', 70, 'D', 2022, 'Semester 1'),
    (10000005, 'TE23042', 82, 'HD', 2022, 'Semester 1'),
    (10000005, 'TE23043', 77, 'CR', 2022, 'Semester 1'),
    (10000005, 'TE23044', 60, 'P', 2022, 'Semester 2'),
    (10000005, 'TE23045', 85, 'HD', 2022, 'Semester 2'),
    (10000005, 'TE23046', 90, 'HD', 2023, 'Semester 1'),
    (10000005, 'TE23047', 55, 'P', 2023, 'Semester 1'),
    (10000005, 'TE23048', 34, 'F', 2023, 'Semester 2'),
    (10000005, 'TE23049', 45, 'F', 2023, 'Semester 2')
""")


# Insert more data for student with ID 10000006
cursor.execute("""
-- Insert data for student with ID 10000006
INSERT INTO STUDENT_UNIT (Student_ID, Course_Unit_Code, Result_Score, Result_Grade, Year_Attempted, Semester_Attempted)
VALUES 
    (10000006, 'IT23034', 85, 'HD', 2020, 'Semester 1'),
    (10000006, 'IT23035', 76, 'D', 2020, 'Semester 1'),
    (10000006, 'IT23036', 92, 'HD', 2020, 'Semester 2'),
    (10000006, 'IT23037', 48, 'F', 2020, 'Semester 2'), 
    (10000006, 'IT23038', 40, 'F', 2021, 'Semester 1'),
    (10000006, 'IT23039', 78, 'D', 2021, 'Semester 1'),
    (10000006, 'IT23037', 72, 'D', 2021, 'Semester 2'),
    (10000006, 'IT23040', 95, 'HD', 2021, 'Semester 2'),
    (10000006, 'IT23041', 65, 'CR', 2021, 'Semester 2'),
    (10000006, 'IT23038', 70, 'D', 2022, 'Semester 1'),
    (10000006, 'IT23042', 82, 'HD', 2022, 'Semester 1'),
    (10000006, 'IT23043', 77, 'CR', 2022, 'Semester 1'),
    (10000006, 'IT23044', 60, 'P', 2022, 'Semester 2'),
    (10000006, 'IT23045', 85, 'HD', 2022, 'Semester 2'),
    (10000006, 'IT23046', 90, 'HD', 2023, 'Semester 1'),
    (10000006, 'IT23047', 55, 'P', 2023, 'Semester 1'),
    (10000006, 'IT23048', 75, 'D', 2023, 'Semester 2'),
    (10000006, 'IT23049', 78, 'D', 2023, 'Semester 2')
""")


# Insert more data for student with ID 10000007
cursor.execute("""
-- Insert data for student with ID 10000007
INSERT INTO STUDENT_UNIT (Student_ID, Course_Unit_Code, Result_Score, Result_Grade, Year_Attempted, Semester_Attempted)
VALUES 
    (10000007, 'CS23034', 70, 'D', 2020, 'Semester 1'),
    (10000007, 'CS23035', 88, 'HD', 2020, 'Semester 1'),
    (10000007, 'CS23036', 65, 'CR', 2020, 'Semester 2'),
    (10000007, 'CS23037', 42, 'F', 2020, 'Semester 2'), 
    (10000007, 'CS23038', 30, 'CR', 2021, 'Semester 1'),
    (10000007, 'CS23039', 78, 'D', 2021, 'Semester 1'),
    (10000007, 'CS23037', 82, 'HD', 2021, 'Semester 2'),
    (10000007, 'CS23040', 95, 'HD', 2021, 'Semester 2'),
    (10000007, 'CS23041', 65, 'CR', 2021, 'Semester 2'),
    (10000007, 'CS23038', 70, 'D', 2022, 'Semester 1'),
    (10000007, 'CS23042', 82, 'HD', 2022, 'Semester 1'),
    (10000007, 'CS23043', 77, 'CR', 2022, 'Semester 1'),
    (10000007, 'CS23044', 60, 'P', 2022, 'Semester 2'),
    (10000007, 'CS23045', 85, 'HD', 2022, 'Semester 2'),
    (10000007, 'CS23046', 90, 'HD', 2023, 'Semester 1'),
    (10000007, 'CS23047', 55, 'P', 2023, 'Semester 1'),
    (10000007, 'CS23048', 45, 'F', 2023, 'Semester 2'),
    (10000007, 'CS23049', 48, 'F', 2023, 'Semester 2')
""")

# Insert more data for student with ID 10000008
cursor.execute("""
-- Insert data for student with ID 10000008
INSERT INTO STUDENT_UNIT (Student_ID, Course_Unit_Code, Result_Score, Result_Grade, Year_Attempted, Semester_Attempted)
VALUES 
    (10000008, 'DS23034', 70, 'D', 2020, 'Semester 1'),
    (10000008, 'DS23035', 88, 'HD', 2020, 'Semester 1'),
    (10000008, 'DS23036', 65, 'CR', 2020, 'Semester 2'),
    (10000008, 'DS23037', 22, 'F', 2020, 'Semester 2'), 
    (10000008, 'DS23038', 40, 'F', 2021, 'Semester 1'),
    (10000008, 'DS23039', 78, 'D', 2021, 'Semester 1'),
    (10000008, 'DS23037', 82, 'HD', 2021, 'Semester 2'),
    (10000008, 'DS23040', 95, 'HD', 2021, 'Semester 2'),
    (10000008, 'DS23041', 65, 'CR', 2021, 'Semester 2'),
    (10000008, 'DS23038', 70, 'D', 2022, 'Semester 1'),
    (10000008, 'DS23042', 82, 'HD', 2022, 'Semester 1'),
    (10000008, 'DS23043', 77, 'CR', 2022, 'Semester 1'),
    (10000008, 'DS23044', 60, 'P', 2022, 'Semester 2'),
    (10000008, 'DS23045', 85, 'HD', 2022, 'Semester 2'),
    (10000008, 'DS23046', 90, 'HD', 2023, 'Semester 1'),
    (10000008, 'DS23047', 55, 'P', 2023, 'Semester 1'),
    (10000008, 'DS23048', 75, 'D', 2023, 'Semester 2'),
    (10000008, 'DS23049', 78, 'D', 2023, 'Semester 2')
""")


# Commit the changes
database.commit()

# Close the cursor and database connection
cursor.close()

database.close()

