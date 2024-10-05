import faker

fake = faker.Faker()

class Student:
    def __init__(self, name: str = None, start_date: str = None, average_grade: float = None, comment: str = None, deleted: bool = False, random: bool = False):
        
        if random:
            self.name = fake.name() + " " + fake.last_name() + " " + fake.suffix() + " " + str(fake.random_int(min=1, max=10000))
            self.start_date = fake.date()
            self.average_grade = fake.random_int(min=1, max=100) / 10
            self.comment = fake.text()
            self.deleted = False
        else:
            self.name = name
            self.start_date = start_date
            self.average_grade = average_grade
            self.comment = comment
            self.deleted = deleted

    def __str__(self) -> str:
        return f"Student(name={self.name}, start_date={self.start_date}, average_grade={self.average_grade}, comment={self.comment}, deleted={self.deleted})"

if __name__ == "__main__":
    student = Student("John Doe", "2022-01-01", 8.5, "Good student", False)
    print(student)
    student = Student(random=True)
    print(student)
