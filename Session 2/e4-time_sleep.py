from event_loop_basic import add_task, event_loop
import time


def task1():
    print("Let's annoy the other task")
    start_time = time.time()
    delay = 5
    while time.time() < start_time + delay:
        pass


def task2():
    print("Let's wait :(")


add_task(task1)
add_task(task2)
event_loop()
