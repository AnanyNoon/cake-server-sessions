from collections import deque
import time

tasks = deque()


def event_loop():
    while tasks:
        task, start, args = tasks.popleft()
        if time.time() < start:
            tasks.append((task, start, args))
        else:
            task(*args)


def add_task(
    task,
    *args,
    callback: int = 0,
):
    tasks.append((task, time.time() + callback, args))
