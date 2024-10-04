DB_FILE = "data.txt"

from students import Student

def create_student(student: Student):
    student_line = student.to_line()
    with open(DB_FILE, "a") as file:
        file.write(f"{len(student_line)};{student_line}")


def read_student(student_name: str) -> Student | None:
    with open(DB_FILE, "r") as file:        
        number = ""
        ret_student = None
        while (char := file.read(1)) != "":
            if char == ";":
                number = int(number)
                student = Student.from_line(file.read(number))
                if student.name == student_name:
                    ret_student = student
                number = ""
            else:
                number += char
    return ret_student

def update_student(student: Student):
    with open(DB_FILE, "a") as file:
        file.write(student.to_line())

def delete_student(student: Student):
    student.deleted = True
    with open(DB_FILE, "a") as file:
        file.write(student.to_line())

def reset_db():
    with open(DB_FILE, "w") as file:
        file.write("")

if __name__ == "__main__":
    reset_db()
    student = Student("John Doe", "2022-01-01", 8.5, "Good student", False)
    create_student(student)
    student = read_student("John Doe")
    student.average_grade = 9.0
    update_student(student)
    delete_student(student)