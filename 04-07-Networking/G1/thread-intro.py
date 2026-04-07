import threading
import time

def count(identifier, end=20):
    number = 0
    while number < end:
        number += 1
        print(time.time(), identifier, number)
        time.sleep(1)

t1 = threading.Thread(target=count, args=("Thread1", 10) )
t1.start()

t2 = threading.Thread(target=count, args=("Thread2", 15) )
t2.start()

# count("Main Thread", 5)

t1.join()
t2.join()

