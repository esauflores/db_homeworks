class Student:
    def __init__(self, name: str, start_date: str, average_grade: float, comment: str, deleted: bool):
        self.name = name
        self.start_date = start_date
        self.average_grade = average_grade
        self.comment = comment
        self.deleted = False

    def __str__(self) -> str:
        return f"Student(name={self.name}, start_date={self.start_date}, average_grade={self.average_grade}, comment={self.comment}, deleted={self.deleted})"

    def to_line(self) -> str:
        data = ["name", "start_date", "average_grade", "comment", "deleted"]
        line = ""
        for item in data:
            item_data = str(getattr(self, item))
            line += f"{len(item_data)};{item_data}"

        return line

    @staticmethod
    def from_line(line: str) -> "Student":
        data = ["name", "start_date", "average_grade", "comment", "deleted"]
        result = []
        
        index = 0
        for item in data:
            next_index = line.index(";", index)
            len_data = int(line[index:next_index])
            result.append(line[next_index + 1 : next_index + len_data + 1])
            index = next_index + len_data + 1

        return Student(result[0], result[1], result[2], result[3], result[4])


if __name__ == "__main__":
    student = Student("John Doe", "2022-01-01", 8.5, "Good student", False)
    print(student.to_line())
    print(student.from_line(student.to_line()))
