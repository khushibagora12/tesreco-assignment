## custom exceptions, used in intern class
class InvalidEmailError(Exception):
    def __init__(self, error_message):
        super().__init__(error_message)

class InvalidDurationError(Exception):
    def __init__(self, error_message):
        super().__init__(error_message)