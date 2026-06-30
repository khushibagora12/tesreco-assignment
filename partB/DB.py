import sqlite3

connection = sqlite3.connect('interns.db', check_same_thread=False)
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Interns(
        id Integer primary Key Autoincrement,
        name Text,
        email Text,
        domain Text
    )
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Mentors(
        id Integer primary Key Autoincrement,
        domain Text,
        mentor Text
    )
''')
connection.commit()

def add_intern(data):
    print("in add intern ", data['name'])
    try:
        cursor.execute('INSERT INTO Interns(name, email, domain) VALUES(?, ?, ?)', (data['name'], data['email'], data['domain']))
        connection.commit()
        return "intern added"
    except Exception as e:
        print("error in inserting data ", e)
        return "error"


def update_intern(id, data):
    try:
        cursor.execute('UPDATE Interns SET name = ?, email = ?, domain = ? WHERE id = ?', (data['name'], data['email'], data['domain'], id))
        connection.commit()
        return "intern updated"
    except Exception as e:
        print("error in inserting data ", e)
        return "error"


def delete_data(id):
    print("in delete data")
    try:
        cursor.execute('DELETE FROM Interns WHERE id = ?', (id,))
        connection.commit()
        print("rows affected: ", cursor.rowcount)
        return "intern deleted"
    except Exception as e:
        print("error in deleting data ", e)
        return "error"
    
    
def get_all():
    print("int getall")
    try:
        cursor.execute('SELECT * FROM Interns')
        data = cursor.fetchall()
        return data
    except Exception as e:
        print("error in getting data ", e)
        return "error"
    
def assign_mentor(domain, mentor):
    try:
        cursor.execute('INSERT INTO Mentors(domain, mentor) VALUES(?, ?)', (domain, mentor))
        connection.commit()
        return "mentor assigned"
    except Exception as e:
        print("error in assigning mentor ", e)
        return "error"
    
def get_mentors():
    try:
        cursor.execute('SELECT * FROM Mentors')
        data = cursor.fetchall()
        return data
    except Exception as e:
        print("error in getting data ", e)
        return "error"

def delete_mentor(id):
    try:
        cursor.execute('DELETE FROM Mentors WHERE id = ?', (id,))
        connection.commit()
        print("row affected: ",cursor.rowcount)
        return "mentor deleted"
    except Exception as e:
        print("error in deleting data ", e)
        return "error"