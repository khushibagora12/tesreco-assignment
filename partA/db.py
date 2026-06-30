import sqlite3

connection = sqlite3.connect('interns.db')
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Interns(
        itern_id Text Primary Key,
        name Text,
        email Text,
        domain Text,
        mentors Text,
        mentor_id Text,
        specialization Text
    )
''')

connection.commit()

def add_intern(data):
    try:
        cursor.execute('INSERT INTO Interns(name, email, domain, mentors, mentor_id, specialization) VALUES(?, ?, ?, ?, ?, ?, ?)', (data['intern_id'], data['name'], data['email'], data['domain'], data['mentors'], data['mentor_id'], data['specialization']))
        connection.commit()
        return "intern added"
    except:
        print("error in inserting data")
        return "error"

def read_data(id):
    try:
        cursor.execute('SELECT * FROM Interns WHERE intern_id = ?', (id,))
        return "success"
    except:
        print("error in reading data")
        return "error"

def delete_data(id):
    try:
        cursor.execute(' DELETE FROM Interns WHERE intern_id = ?', (id,))
        connection.commit()
        return "intern deleted"
    except:
        print("error in deleting data")
        return "error"
    
def update_data(id, data):
    try:
        cursor.execute('UPDATE Interns SET name=? WHERE intern_id = ?', (data['name'], id))
        connection.commit()
        return "intern deleted"
    except:
        print("error in deleting data")
        return "error"