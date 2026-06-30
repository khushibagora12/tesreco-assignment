import csv
import datetime
def mark_attendence(data):
    with open(f"{datetime.datetime.now().date()}.csv", 'a', newline='') as at:
        writer = csv.writer(at)
        writer.writerow([datetime.datetime.now().time(), data['name'], data['status']]);