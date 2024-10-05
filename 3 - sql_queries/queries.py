import sqlite3
import numpy as np
from prettytable import PrettyTable


conn = sqlite3.connect('harbour2.db')

# set row factory to return rows as dictionaries
conn.row_factory = sqlite3.Row

def print_as_table(results):
    table = PrettyTable()
    table.field_names = results[0].keys()
    for row in results:
        table.add_row(row)
    print(table)


print("All the students named Lisa Lyons: ")
cursor = conn.execute(
  """
  SELECT students.id, students.name as student
  FROM students
  WHERE name = 'Lisa Lyons'
  LIMIT 10
  """
)
query1 = cursor.fetchall()
print_as_table(query1)
print()

print("All the students who entered after 2020: ")
cursor = conn.execute(
  """
  SELECT students.id, students.name as student, students.entrance_year as 'entrance year'
  FROM students
  WHERE entrance_year > 2020 
  ORDER BY students.entrance_year ASC, students.name ASC
  LIMIT 10
  """
)
query2 = cursor.fetchall()
print_as_table(query2)
print()


print("All Students names from CS who entered before 2020: ")
cursor = conn.execute(
  """
  SELECT students.id, students.name as student, students.entrance_year as 'entrance year'
  FROM students
  INNER JOIN majors ON students.major_id = majors.id 
  WHERE majors.name = 'CS' AND students.entrance_year < 2020
  ORDER BY students.name ASC
  LIMIT 10
  """
)
query3 = cursor.fetchall()
print_as_table(query3)
print()

print("All students names and their entrance year who entered between 2017 and 2019: ")
cursor = conn.execute(
  """
  SELECT students.id, students.name as student, students.entrance_year as 'entrance year'
  FROM students
  WHERE students.entrance_year >= 2017 AND students.entrance_year <= 2019
  ORDER BY students.entrance_year ASC, students.name ASC
  LIMIT 10
  """
)
query4 = cursor.fetchall()
print_as_table(query4)
print()

print("All students names and their entrance year who entered in a leap year: ")
cursor = conn.execute(
  """
  SELECT students.id, students.name as student, students.entrance_year as 'entrance year'
  FROM students
  WHERE students.entrance_year % 4 = 0
  ORDER BY students.entrance_year ASC, students.name ASC
  LIMIT 10
  """
)
query5 = cursor.fetchall()
print_as_table(query5)
print()

print("All the teachers who have more than 3 years of experience: ")
cursor = conn.execute(
  """
  SELECT teachers.id, teachers.name as teacher, teachers.experience_years as 'experience years'
  FROM teachers
  WHERE teachers.experience_years > 3
  ORDER BY teachers.name ASC
  LIMIT 10
  """
)
query6 = cursor.fetchall()
print_as_table(query6)
print()

print("All students names and their major names who entered in 2020: ")
cursor = conn.execute(
  """
  SELECT students.id, students.name as student, majors.name as major, students.entrance_year as 'entrance year'
  FROM students
  INNER JOIN majors ON students.major_id = majors.id
  WHERE students.entrance_year = 2020
  ORDER BY majors.name ASC, students.name ASC
  LIMIT 10
  """
)
query7 = cursor.fetchall()
print_as_table(query7)
print()

print("All students names and their major names who have the name starting with 'Thomas': ")
cursor = conn.execute(
  """
  SELECT students.id, students.name as student, majors.name as major
  FROM students
  INNER JOIN majors ON students.major_id = majors.id
  WHERE students.name LIKE 'Thomas%'
  ORDER BY majors.name ASC, students.name ASC
  LIMIT 10
  """
)
query8 = cursor.fetchall()
print_as_table(query8)
print()

print("All students names and their major names who have a full name length less than 10: ")
cursor = conn.execute(
  """
SELECT students.id, students.name as student, majors.name as major
  FROM students
  INNER JOIN majors ON students.major_id = majors.id
  WHERE length(students.name) < 10
  ORDER BY majors.name ASC, students.name ASC
  LIMIT 10
  """
)
query9 = cursor.fetchall()
print_as_table(query9)
print()