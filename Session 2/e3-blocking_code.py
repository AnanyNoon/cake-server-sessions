from event_loop_basic import add_task, event_loop


def task1(cnt: int):
    for i in range(cnt):
        # I/O blocking
        print(f"Task 1 {i + 1}")


def task2(cnt: int):
    for i in range(cnt):
        # I/O blocking
        print(f"Task 2 {i + 1}")


add_task(task1, 5)
add_task(task2, 5)
event_loop()
