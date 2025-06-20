from time import perf_counter


class Timer():
    def __enter__(self):
        self.start = perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.elapsed = perf_counter() - self.start


from time import sleep

with Timer() as timer:
    sleep(0.7)
    sleep(1.5)
print('Затраченное время:', timer.elapsed)


class Timer():
    def __enter__(self):
        self.start = perf_counter()
        self.end = 0.0
        return lambda : self.end - self.start

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = perf_counter()


from time import sleep

with Timer() as timer:
    # sleep(0.7)
    sleep(1.5)
print('Затраченное время:', timer())


from time import perf_counter, sleep

class Timer:
    def __enter__(self):
        self.start = perf_counter()
        self.end = 0.0
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.end = perf_counter()

    def __call__(self):
        return self.end - self.start


with Timer() as timer:
    sleep(0.7)
    sleep(1.5)
print('Затраченное время:', timer())

from time import perf_counter, sleep


class Timer:
    def __enter__(self):
        print('Вход в контекст'.center(30, '-'))
        self.start = perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print('Затраченное время:', perf_counter() - self.start)
        print('Выход из контекста'.center(30, '-'))


with Timer():
    print('Выполнение какой-то задачи ...')
    sleep(0.7)
    sleep(1.5)




class Trace:
    def __enter__(self):
        print('Начало выполнения блока with')

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_value:
            print(f'Во время выполнения блока with было возбуждено исключение {exc_value}')
        print('Конец выполнения блока with')
        return True                           # обрабатываем все типы исключений


class WritableTextFile:
    def __init__(self, path):
        self.path = path

    def __enter__(self):
        self.file = open(self.path, mode='w', encoding='utf-8')
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()



import sys

class RedirectedStdout:
    def __init__(self, new_output):
        self.new_output = new_output

    def __enter__(self):
        self.standard_output = sys.stdout
        sys.stdout = self.new_output

    def __exit__(self, exc_type, exc_value, traceback):
        sys.stdout = self.standard_output
