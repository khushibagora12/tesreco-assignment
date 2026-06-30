class GenerateCertificates:
    def __init__(self, name):
        self.name = name

    def generate(self):
        yield f"Certificate Generated for {self.name}"