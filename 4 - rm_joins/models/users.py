
class User:
    def __init__(self, name: str, email: str, password: str, created_at: str, user_id: int = 0, deleted: bool = False):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password
        self.created_at = created_at
        self.deleted = deleted

    def __str__(self) -> str:
        return f"User(user_id={self.user_id}, name={self.name}, email={self.email}, password={self.password}, deleted={self.deleted})"
