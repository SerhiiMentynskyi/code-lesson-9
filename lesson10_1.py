import sqlite3
connection = sqlite3.connect('database.sl3')
cur = connection.cursor()
# cur.execute('CREATE TABLE Student (name TEXT, mark INT);')

# cur.execute('INSERT INTO Student (name, mark) Values ("Garry",11)')
# cur.execute('UPDATE Student SET mark = 1 WHERE name = "Nedilia"')
# cur.execute('UPDATE Student SET name = "Denys" WHERE rowid = 3')

cur.execute('DELETE from Student WHERE rowid = 4')

cur.execute('Select * From Student')
connection.commit()

students = cur.fetchall()
print(students)

connection.close()


