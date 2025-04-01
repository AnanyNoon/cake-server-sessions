from event_loop_basic import add_task, event_loop


def task3():
    print("Failed to annoy the other task :(")


def task1():
    print("Let's annoy the other task")
    add_task(task3, callback=5)


def task2():
    print("I didn't wait :)")


add_task(task1)
add_task(task2)
event_loop()
