from q1_5_intern import Intern
import csv

intern = Intern("kay", "kb@gmail.com", "ML", "4")

def add(self):
    self.store_details()
    
def store_details(intern):
    with open('interns.csv', 'a', newline='') as csvFile:
        data = csv.writer(csvFile)
        data.writerow([intern.intern_id, intern.name, intern.email, intern.domain, intern.duration])   

def get_details(id):
    with open('interns.csv', newline='') as csvFile:
        data = csv.reader(csvFile)
        for row in data:
            if id==row[0]: print(row)

def remove(id):
    pass