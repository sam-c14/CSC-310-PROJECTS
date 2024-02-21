import threading
import time

class Philosopher(threading.Thread):
    def __init__(self, index, left_fork, right_fork, semaphore):
        threading.Thread.__init__(self)
        self.index = index
        self.left_fork = left_fork
        self.right_fork = right_fork
        self.semaphore = semaphore

    def run(self):
        for _ in range(3):  # Philosophers will eat three times
            self.think()
            self.eat()

    def think(self):
        print(f"Philosopher {self.index} is thinking.")
        time.sleep(1)

    def eat(self):
        with self.semaphore:
            print(f"Philosopher {self.index} is hungry and trying to pick up forks.")

            with self.left_fork:
                print(f"Philosopher {self.index} picked up the left fork.")
                with self.right_fork:
                    print(f"Philosopher {self.index} picked up the right fork and is eating.")
                    time.sleep(1)
                    print(f"Philosopher {self.index} finished eating and put down forks.")

# Number of philosophers (threads)
num_philosophers = 5

# Create a semaphore to limit the number of philosophers eating at the same time
semaphore = threading.BoundedSemaphore(value=num_philosophers - 1)

# Create forks (locks) for each philosopher
forks = [threading.Lock() for _ in range(num_philosophers)]

# Create philosophers
philosophers = [Philosopher(i, forks[i], forks[(i + 1) % num_philosophers], semaphore) for i in range(num_philosophers)]

# Start the philosophers
for philosopher in philosophers:
    philosopher.start()

# Wait for all philosophers to finish
for philosopher in philosophers:
    philosopher.join()
