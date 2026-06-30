## 1. Intern class
import datetime 
import time
from q3_iterate_id import IterateId
from q4_generate_certificate import GenerateCertificates
from email_validator import validate_email
from q5_intern_exceptions import InvalidDurationError, InvalidEmailError

def logs(func):
    def sub(self):
        print(func)
        print(datetime.datetime.now().time())
        func(self)
        print(datetime.datetime.now().time())

    return sub

class Intern:
    ids = IterateId()
    iteratingIds = iter(ids)

    def __init__(self):
        self.intern_id = next(self.iteratingIds)

    ## setter
    def set_name(self, name):
        self.name = name

    def set_email(self, email):
        try:
            validate = validate_email(email, check_deliverability=False)
            self.email = email
        except:
            raise InvalidEmailError("Incorrect email format")
        
    def set_domain(self, domain):
        self.domain = domain

    def set_duration(self, duration):
        if duration > 12 or duration < 4:
            raise InvalidDurationError("Internship is offered for 4 to 12 weeks only")
        self.duration = duration

    ## getter
    def get_id(self):
        return self.intern_id

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_domain(self):
        return self.domainn

    def get_duration(self):
        return self.durationion
    
    ## str override
    def __str__(self):
        return f"id: {self.intern_id}\nname: {self.name}\nemail: {self.email}\ndomain: {self.domain}\nduration: {self.duration}"
    
## 2. performance function
    @logs
    def calc_performance(self):
        time.sleep(5)
        print("todays work ....")

    ## certificate generation
    def generate_certificate(self):
        certificate = GenerateCertificates(self.name)
        print(next(certificate.generate()))

                    

## Object creation
kb = Intern();
kb.set_name("khushi")
kb.set_email("kb@gmail.com")
kb.set_domain("machine learning")
kb.set_duration(4)
print(kb)
kb.calc_performance()
kb.add()

kb.get_details("TES001")
kb.remove("TES001")
# kay = Intern();
# kay.set_name("kay")
# kay.set_email("kay@gmail.com")
# kay.set_domain("machine learning")
# kay.set_duration("4 weeks")
# print(kay)
# kay.calc_performance()
# kay.generate_certificate()