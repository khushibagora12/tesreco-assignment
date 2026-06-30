## 7. multiple inferitence and method resolution order
class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def __str__(self):
        return self.name + " " + self.email

class Employee:
    def __init__(self, emp_id):
        self.emp_id = emp_id

    def __str__(self):
        return self.emp_id

class Mentor:
    def __init__(self, batch):
        self.batch = batch

    def __str__(self):
        return self.batch

class TESRECOMentor(Person, Employee, Mentor):
    def __init__(self, name, email, emp_id, batch):
        Person.__init__(self, name, email)
        Employee.__init__(self, emp_id)
        Mentor.__init__(self, batch)
        
    def __str__(self):
        str_p = Person.__str__(self)
        str_e = Employee.__str__(self)
        str_m = Mentor.__str__(self)

        return str_p + " " + str_e + " " + str_m

obj = TESRECOMentor("kb", "kbgm", "101", "mwf")
print(obj)