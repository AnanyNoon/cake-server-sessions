from event_loop_basic import add_task, event_loop


def task1():
    print("Task 1")


def task2():
    print("Task 2")


add_task(task1)
add_task(task2)
event_loop()
