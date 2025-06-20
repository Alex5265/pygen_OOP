from time import perf_counter, sleep
from contextlib import contextmanager

@contextmanager
def timer():
    start = perf_counter()
    end = 0
    yield lambda : (end - start)
    end = perf_counter()

with timer() as manager:
    sleep(1.4)
    print(manager())            # вызов внутри блока with

print(manager())                # вызов после блока with

