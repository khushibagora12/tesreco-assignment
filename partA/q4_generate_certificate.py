## generator to create certificates one at a time, used in intern class
class Generate_certificates:
    def __init__(self, name):
        self.name = name

    def generate(self):
        yield f"Certificate Generated for {self.name}"