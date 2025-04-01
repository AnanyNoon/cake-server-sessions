def task():
    for i in range(1, 10):
        yield i


t = task()
print(t)
for i in range(1, 10):
    print(next(t))
