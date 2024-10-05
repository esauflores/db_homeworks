DB_FILE = "data.db"

import sqlite3

from students import Student

conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

def create_student(student: Student):
    cursor.execute("INSERT INTO students (name, start_date, average_grade, comment, deleted) VALUES (?, ?, ?, ?, ?)", (student.name, student.start_date, student.average_grade, student.comment, student.deleted))
    conn.commit()


def read_student(student_name: str) -> Student | None:
    cursor.execute("SELECT * FROM students WHERE name = ?", (student_name,))
    result = cursor.fetchone()
    if result:
        return Student(*result)
    return None

def update_student(student: Student):
    cursor.execute("UPDATE students SET average_grade = ? WHERE name = ?", (student.average_grade, student.name))
    conn.commit()

def delete_student(student: Student):
    cursor.execute("UPDATE students SET deleted = ? WHERE name = ?", (student.deleted, student.name))
    conn.commit()

def delete_student(student: Student):
    cursor.execute("DELETE FROM students WHERE name = ?", (student.name,))
    conn.commit()

def create_students(students: list[Student]):
    cursor.executemany("INSERT INTO students (name, start_date, average_grade, comment, deleted) VALUES (?, ?, ?, ?, ?)", [(student.name, student.start_date, student.average_grade, student.comment, student.deleted) for student in students])
    conn.commit()

def reset_db():
    cursor.execute("CREATE TABLE IF NOT EXISTS students (name TEXT, start_date TEXT, average_grade REAL, comment TEXT, deleted BOOLEAN)")
    conn.commit()
    
    cursor.execute("DELETE FROM students")
    conn.commit()
    

if __name__ == "__main__":
    reset_db()
    student = Student(name="John Doe", start_date="2022-01-01", average_grade=8.5, comment="Good student", deleted=False)
    create_student(student)
    student = read_student("John Doe")
    student.average_grade = 9.0
    update_student(student)
    delete_student(student)
