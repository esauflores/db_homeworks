import sqlite3
import numpy as np
from prettytable import PrettyTable


conn = sqlite3.connect('data.db')

# set row factory to return rows as dictionaries
conn.row_factory = sqlite3.Row

def print_as_table(results):
    table = PrettyTable()
    table.field_names = results[0].keys()
    for row in results:
        table.add_row(row)
    print(table)
    print()


print("Users with number of files: ")
cursor = conn.execute(
  """
  SELECT users.user_id, users.name as user, COUNT(files.file_id) as "number of files"
  FROM users
  LEFT JOIN files ON users.user_id = files.user_id
  GROUP BY users.user_id
  ORDER BY "number of files" DESC
  LIMIT 10
  """
)
query1 = cursor.fetchall()
print_as_table(query1)

print("Number of versions per file: ")
cursor = conn.execute(
  """
  SELECT files.file_id, files.name as file, COUNT(file_versions.file_version_id) as "number of versions"
  FROM files
  LEFT JOIN file_versions ON files.file_id = file_versions.file_id
  GROUP BY files.file_id
  ORDER BY "number of versions" DESC
  LIMIT 10
  """
)
query2 = cursor.fetchall()
print_as_table(query2)

print("Users without files: ")
cursor = conn.execute(
  """
  SELECT users.user_id, users.name as user, COUNT(files.file_id) as "number of files"
  FROM users
  LEFT JOIN files ON users.user_id = files.user_id
  WHERE files.file_id IS NULL
  LIMIT 10
  """
)
query3 = cursor.fetchall()
print_as_table(query3)

print("Files with versions created in december 2024: ")
cursor = conn.execute(
  """
  SELECT files.file_id, files.name as file, file_versions.created_at as "created at"
  FROM files
  JOIN file_versions ON files.file_id = file_versions.file_id
  WHERE file_versions.created_at LIKE '%2024-12%'
  LIMIT 10
  """
)
query4 = cursor.fetchall()
print_as_table(query4)

print("Files with versions created in december 2024: ")
cursor = conn.execute(
  """
  SELECT files.file_id, files.name as file, file_versions.created_at as "created at"
  FROM files
  JOIN file_versions ON files.file_id = file_versions.file_id
  WHERE file_versions.created_at LIKE '%2024-12%'
  LIMIT 10
  """
)
query5 = cursor.fetchall()
print_as_table(query5)


print("Users with most versions: ")
cursor = conn.execute(
  """
  SELECT users.user_id, users.name as user, COUNT(file_versions.file_version_id) as "number of versions"
  FROM users
  JOIN files ON users.user_id = files.user_id
  JOIN file_versions ON files.file_id = file_versions.file_id
  GROUP BY users.user_id
  ORDER BY "number of versions" DESC
  LIMIT 10
  """
)
query6 = cursor.fetchall()
print_as_table(query6)


print("Users joined after july 2024: ")
cursor = conn.execute(
  """
  SELECT users.user_id, users.name as user, users.created_at as "joined at"
  FROM users
  WHERE users.created_at > '2024-07-01'
  ORDER BY users.created_at ASC
  LIMIT 10
  """
)
query7 = cursor.fetchall()
print_as_table(query7)


