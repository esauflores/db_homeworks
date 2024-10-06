class File:
    def __init__(self, name: str, password: str, user_id: int, created_at: str, file_id: int = 0, deleted: bool = False):
        self.file_id = file_id
        self.name = name
        self.password = password
        self.user_id = user_id
        self.created_at = created_at
        self.deleted = deleted

    def __str__(self) -> str:
        return f"File(file_id={self.file_id}, name={self.name}, user_id={self.user_id}, deleted={self.deleted})"


