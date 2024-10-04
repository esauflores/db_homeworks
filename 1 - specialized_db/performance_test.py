from students import Student
from database import create_student, read_student, update_student, delete_student, reset_db
import faker
from time import time

reset_db()
fake = faker.Faker()

STUDENTS_COUNT = 1000000

# Calculate checkpoint interval
checkpoint_interval = STUDENTS_COUNT // 10


for i in range(STUDENTS_COUNT):
    student = (Student(fake.name() + str(fake.random_int(0, 10000)), fake.date(), fake.random_int(0, 10), fake.text(), False))
    create_student(student)
    # if (i + 1) % checkpoint_interval == 0:
    #     print(f"Checkpoint: Created {i + 1} students")

# measure time of all crud

# 1 create
student = Student(fake.name() + str(fake.random_int(0, 10000)), fake.date(), fake.random_int(0, 10), fake.text(), False)
time_start = time()
create_student(student)
time_end = time()
print(f"1 create: {time_end - time_start}")

# 2 read
time_start = time()
student = read_student(student.name)
time_end = time()
print(f"2 read: {time_end - time_start}")

# 3 update
student.grade = fake.random_int(0, 10)
student.comment = fake.text()
time_start = time()
update_student(student)
time_end = time()
print(f"3 update: {time_end - time_start}")

# 4 delete
student.deleted = True
time_start = time()
delete_student(student)
time_end = time()
print(f"4 delete: {time_end - time_start}")
