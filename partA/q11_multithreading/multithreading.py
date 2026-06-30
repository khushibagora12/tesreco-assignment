from threading import Thread
from attendanceProcessing import attendence_processing
from certificateGeneration import certificate_generation

t1 = Thread(target=attendence_processing, args=("khushi", "present"))
t2 = Thread(target=certificate_generation, args=("khushi",))

t1.start()
t2.start()