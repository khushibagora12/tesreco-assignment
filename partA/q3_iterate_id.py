## custom iterator for generating ids, used in intern class
class IterateId:
    def __init__(self):
        self.id = "001"

    def __iter__(self):
        return self
    
    def __next__(self):
        x = self.id

        digit = (int)(x) + 1

        self.id = f"{digit:03d}"
        return f"TES{x}";