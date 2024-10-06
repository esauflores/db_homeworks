import sqlite3
from mimesis import Generic  # Changed from Faker to Mimesis

generic = Generic()  # Initialize Mimesis Generic instance

from models.users import User
from models.files import File
from models.file_versions import FileVersion

conn = sqlite3.connect('data.db')
cursor = conn.cursor()

USERS_COUNT = 10000
FILES_COUNT = 10000
FILE_VERSIONS_COUNT = 1000

def create_table_user():
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        password TEXT NOT NULL,
        created_at TEXT NOT NULL,
        deleted BOOLEAN NOT NULL
    )''')
    
    conn.commit()

def create_table_file():
    cursor.execute('''CREATE TABLE IF NOT EXISTS files (
        file_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        password TEXT NOT NULL,
        user_id INTEGER NOT NULL REFERENCES users(user_id),
        created_at TEXT NOT NULL,
        deleted BOOLEAN NOT NULL
    )''')

    conn.commit()

def create_table_file_version():
    cursor.execute('''CREATE TABLE IF NOT EXISTS file_versions (
        file_version_id INTEGER PRIMARY KEY AUTOINCREMENT,
        file_id INTEGER NOT NULL REFERENCES files(file_id),
        file_url TEXT NOT NULL,
        created_at TEXT NOT NULL,
        deleted BOOLEAN NOT NULL
    )''')

    conn.commit()


def reset_db():
    cursor.execute('''DROP TABLE IF EXISTS file_versions''')
    cursor.execute('''DROP TABLE IF EXISTS files''')
    cursor.execute('''DROP TABLE IF EXISTS users''')

    create_table_user()
    create_table_file()
    create_table_file_version()

    conn.commit()

def fill_table_users_with_passwords(users_count: int) -> tuple[list[User], list[str]]:
    users = []
    passwords = []

    for _ in range(users_count):
        password = generic.text.word()  # Changed to use Mimesis for password
        passwords.append(password)
        user = User(name=generic.person.full_name(),  # Changed to use Mimesis for name
                    email=generic.person.email(),  # Changed to use Mimesis for email
                    password=password,
                    created_at=generic.datetime.datetime().isoformat())  # Changed to use Mimesis for datetime
        users.append(user)
            
    users_to_insert = [(user.name, user.email, user.password, user.created_at, user.deleted) for user in users]
    cursor.executemany('''INSERT INTO users (name, email, password, created_at, deleted) VALUES (?, ?, ?, ?, ?)''', users_to_insert)
    conn.commit()
    
    return users, passwords

def fill_table_files(users: list[User], files_count: int) -> list[File]:
    files = []

    for _ in range(files_count):
        file = File(name=generic.file.file_name(),  # Changed to use Mimesis for file name
                    password=generic.text.word(),  # Changed to use Mimesis for password
                    user_id=generic.random.randint(0, len(users) - 1),  # Changed to use Mimesis for random int
                    created_at=generic.datetime.datetime().isoformat())  # Changed to use Mimesis for date_time
        files.append(file)
        
    files_to_insert = [(file.name, file.password, file.user_id, file.created_at, file.deleted) for file in files]
    cursor.executemany('''INSERT INTO files (name, password, user_id, created_at, deleted) VALUES (?, ?, ?, ?, ?)''', files_to_insert)
        
    conn.commit()
    
    return files

def fill_table_file_versions(files: list[File], file_versions_count: int) -> list[FileVersion]:
    file_versions = []

    for _ in range(file_versions_count):
        file_version = FileVersion(file_id=generic.random.randint(0, len(files) - 1),  # Changed to use Mimesis for random int
                                   file_url=f"/{generic.text.word()}/{generic.file.file_name()}",  # Changed to use Mimesis for file path
                                   created_at=generic.datetime.datetime().isoformat(),  # Changed to use Mimesis for date_time
                                   deleted=False)
        file_versions.append(file_version)
   
    file_versions_to_insert = [(file_version.file_id, file_version.file_url, file_version.created_at, file_version.deleted) for file_version in file_versions]
    cursor.executemany('''INSERT INTO file_versions (file_id, file_url, created_at, deleted) VALUES (?, ?, ?, ?)''', file_versions_to_insert)
    conn.commit()

    return file_versions
    
if __name__ == '__main__':
    print("Reseting db")
    reset_db()
    print("Reset db")
    
    print(f"Creating {USERS_COUNT} users")
    users, passwords = fill_table_users_with_passwords(USERS_COUNT)
    print(f"Created {USERS_COUNT} users")
    
    print(f"Creating {FILES_COUNT} files")
    files = fill_table_files(users, FILES_COUNT)
    print(f"Created {FILES_COUNT} files")
    
    print(f"Creating {FILE_VERSIONS_COUNT} file versions")
    file_versions = fill_table_file_versions(files, FILE_VERSIONS_COUNT)
    print(f"Created {FILE_VERSIONS_COUNT} file versions")
