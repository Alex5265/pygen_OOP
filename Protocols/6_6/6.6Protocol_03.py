# Контекстный менеджер safe_write
# Реализуйте контекстный менеджер safe_write с помощью декоратора @contextmanager, который принимает один аргумент:
#
# filename — имя файла
# Контекстный менеджер должен позволять записывать информацию в файл с именем filename. Причем если во время записи в файл было возбуждено какое-либо исключение, контекстный менеджер должен поглотить его, отменить все выполненные ранее записи в файл, если они были, вернуть файл в исходное состояние и проинформировать о возбужденном исключении выводом следующего текста:
#
# Во время записи в файл было возбуждено исключение <тип исключения>
# Примечание 1. Наглядные примеры использования контекстного менеджера safe_write продемонстрированы в тестовых данных.
#
# Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный контекстный менеджер используется только с корректными данными.

from contextlib import  contextmanager

@contextmanager
def safe_write(filename):
    file = open(filename, 'a', encoding='UTF-8')
    cursor = file.tell()
    try:
        yield file
    except Exception as err:
        file.truncate(cursor)
        print('Во время записи в файл было возбуждено исключение', type(err).__name__)
    finally:
        file.close()


with safe_write('undertale.txt') as file:
    file.write('Тень от руин нависает над вами, наполняя вас решительностью')

with open('undertale.txt') as file:
    print(file.read())

with safe_write('under_tale.txt') as file:
    file.write('Тень от руин нависает над вами, наполняя вас решительностью\n')

with safe_write('under_tale.txt') as file:
    print('Под весёлый шорох листвы вы наполняетесь решительностью', file=file, flush=True)
    raise ValueError

with open('under_tale.txt') as file:
    print(file.read())






