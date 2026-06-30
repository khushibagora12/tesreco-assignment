import logging

logging.basicConfig(
    filename='tesreco.log',
    filemode='w',
    level=logging.INFO,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%d-%m-%Y %H:%M:%S'
)

class report_generation:
    def __init__(self, name):
        self.name = name

    def login(self):
        if (len(self.name) < 3):
            logging.warning(f"{self.name} have less then 3 letters")

        print(self.name, " logged in")
        logging.info(f"{self.name} logged in successfully")

    def start_report_generation(self):
        try:
            print("report generation started")
            logging.info(f"report generation started by {self.name}")
        except Exception as e:
            logging.error(f"error: {e}")


    def report_generation_completed(self):
        print("report generation completed")
        logging.info(f"report generation completed for {self.name}")