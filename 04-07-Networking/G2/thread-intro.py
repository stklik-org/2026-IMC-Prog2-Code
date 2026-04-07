import threading
import time

def countUntil(identifier, end=20):
    number = 0

    for _ in range(end):
        number += 1
        print(time.time(), identifier, number)
        time.sleep(1)

# countUntil("Main")
t1 = threading.Thread(target=countUntil, args=("Thread1",))
t1.start()

t2  = threading.Thread(target=countUntil, args=("Thread2",10))
t2.start()

countUntil("Main", 5)

t1.join()
t2.join()