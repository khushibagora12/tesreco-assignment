## 8. Abstract class

from abc import abstractmethod, ABC

class Report(ABC):
    @abstractmethod
    def generate_report(self): pass

class AttendanceReport(Report):
    def generate_report(self):
        print("Attendance report")

class PerformanceReport(Report):
    def generate_report(self):
        print("Performance report")

obj1 = AttendanceReport()
obj1.generate_report()

obj2 = PerformanceReport()
obj2.generate_report()