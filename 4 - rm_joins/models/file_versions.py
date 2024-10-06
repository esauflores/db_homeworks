class FileVersion:
    def __init__(self, file_id: int, file_url: str, created_at: str, file_version_id: int = 0, deleted: bool = False):
        self.file_version_id = file_version_id
        self.file_id = file_id
        self.file_url = file_url
        self.created_at = created_at
        self.deleted = deleted

