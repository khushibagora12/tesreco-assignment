import sqlite3

connection = sqlite3.connect("intern_details.db", check_same_thread=False)

cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS InternsDetail(
        id Integer primary Key Autoincrement,
        name Text,
        email Text,
        domain Text,
        mentor Text,
        mentor_id Integer,
        specialization Text
    )
''')

def add_intern(data):
    cursor.execute('INSERT INTO InternsDetail(name, email, domain, mentor, mentor_id, specialization) VALUES(?, ?, ?, ?, ?, ?)', (data['name'], data['email'], data['domain'], data['mentor'], data['mentor_id'], data['specialization']))
    connection.commit()
    print("intern added")

def update_intern(data, id):
    cursor.execute('UPDATE InternsDetail SET name = ?, email = ?, domain = ?, mentor = ?, mentor_id = ?, specialization = ? WHERE id = ?', (data['name'], data['email'], data['domain'], data['mentor'], data['mentor_id'], data['specialization'], id))
    connection.commit()
    print("intern updated")

def delete_intern(id):
    cursor.execute('DELETE FROM InternsDetail WHERE id = ?', (id,))
    connection.commit()
    print("intern deleted")

def get_interns():
    cursor.execute('SELECT * FROM InternsDetail')
    data = cursor.fetchall()
    for row in data:
        print(row)



i1 = {
    "name" : "kay",
    "email" : "kay@gmail.com",
    "domain" : "ML",
    "mentor" : "mentorA",
    "mentor_id" : 101,
    "specialization" : "ML",
}
i2 = {
    "name" : "alex",
    "email" : "alex@gmail.com",
    "domain" : "devops",
    "mentor" : "mentorC",
    "mentor_id" : 103,
    "specialization" : "devops",
}
add_intern(i1)
add_intern(i2)
get_interns()
delete_intern(2)

updated_data = {
    "name" : "kay",
    "email" : "kay@gmail.com",
    "domain" : "Web dev",
    "mentor" : "mentorB",
    "mentor_id" : 102,
    "specialization" : "Web dev",
}

update_intern(updated_data, 1)
get_interns()