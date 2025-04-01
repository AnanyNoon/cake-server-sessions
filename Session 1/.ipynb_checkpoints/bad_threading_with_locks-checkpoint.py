import threading
import time

counter = 0

Lock = threading.Lock()


def increment():
    global counter
    for _ in range(10_000):  # Smaller number to reduce runtime
        with Lock:
            temp = counter  # Read
            time.sleep(0.0001)  # Force context switch between threads
            counter = temp + 1  # Write (now more likely to be overwritten)


start_time = time.time()
threads = []
for _ in range(4):
    t = threading.Thread(target=increment)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

end_time = time.time()
print(f"Execution time: {end_time - start_time:.2f} seconds")
print(f"Final counter value: {counter}")  # Will almost certainly be incorrect!

counter = 0
start_time = time.time()
for _ in range(40_000):
    temp = counter
    time.sleep(0.0001)
    counter = temp + 1
end_time = time.time()

print(f"Execution time: {end_time - start_time:.2f} seconds")
print(f"Final counter value: {counter}")  # Will almost certainly be incorrect!
