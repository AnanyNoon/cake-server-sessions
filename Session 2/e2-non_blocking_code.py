from event_loop_basic import add_task, event_loop

"""
    Event loop
        [task1(2), task2(2)]

"""


def task1(cnt: int):
    print(f"Task 1 {cnt}")
    if cnt == 5:
        return
    # I/O bound
    add_task(task1, cnt + 1)  # await task1(cnt + 1)


def task2(cnt: int):
    print(f"Task 2 {cnt}")
    if cnt == 5:
        return
    add_task(task2, cnt + 1)  # await task2(cnt+1)


add_task(task1, 1)
add_task(task2, 1)
event_loop()

"""
    task1(1)
    task1(2)
    task1(3)
    task1(4)
    task1(5)
    
    task2(1)
    task2(2)
    task2(3)
    task2(4)
    task2(5)

"""
