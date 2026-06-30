import multiprocessing
from q11_multithreading.certificateGeneration import certificate_generation

list_of_interns = ["kay", "alex", "john"]

if __name__ == "__main__":
    for i in list_of_interns:
        p = multiprocessing.Process(target=certificate_generation, args=(i,))
        p.start()