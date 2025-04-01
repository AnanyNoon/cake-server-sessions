import requests
import threading
import time

total = []


def call_fn(index: int):
    global total
    a = time.time()
    requests.get("http://localhost:8080/").json()
    b = time.time()
    total.append(b - a)


if __name__ == "__main__":
    import sys

    cnt = int(sys.argv[1])

    start_time = time.time()
    threads = []
    total = []
    for i in range(cnt):  # Create n threads
        t = threading.Thread(target=call_fn, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    end_time = time.time()

    total.sort()
    print(
        f"Analysis, max: {total[-1]:.2f}, min: {total[0]:.2f}, avg: {(sum(total) / len(total)):.2f}"
    )
    print(f"Execution time for {cnt} calls: {end_time - start_time:.2f}")
