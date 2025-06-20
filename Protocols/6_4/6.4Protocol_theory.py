# class CustomContextManager:
#     def __enter__(self):
#         print('Вход в контекстный менеджер...')
#         return 'Python generation!'
#
#     def __exit__(self, exc_type, exc_value, traceback):
#         print('Выход из контекстного менеджера...')
#         print(exc_type, exc_value, traceback, sep='\n')
#
#
# class CustomContextManager:
#     def __enter__(self):
#         print('Вход в контекстный менеджер...')
#         return 'Python generation!'
#
#     def __exit__(self, exc_type, exc_value, traceback):
#         print('Выход из контекстного менеджера...')
#         if isinstance(exc_value, IndexError):
#             print(f'Тип возникшего исключения: {exc_type}')
#             print(f'Текст исключения: {exc_value}')
#             return True                                 # подавляем возбужденное исключение IndexError
#         return False                                    # все остальные типы исключений не подавляются
#
#
# with CustomContextManager() as manager:
#     print(manager)
#
#
# with CustomContextManager() as manager:
#     print(manager)
#     print(manager[100])


# with open('output.txt', mode='w', encoding='utf-8') as file:
#     print('__enter__' in dir(file))                      # наличие метода __enter__()
#     print('__exit__' in dir(file))                       # наличие метода __exit__()
#     file.write('Python generation!')


# from decimal import Decimal, localcontext
#
# num1 = Decimal('1')
# num2 = Decimal('9')
#
# print(num1 / num2)                   # по умолчанию 28 знаков после запятой
#
# with localcontext() as ctx:
#     ctx.prec = 5                     # устанавливаем 5 знаков после запятой
#     print(num1 / num2)
#
# with localcontext() as ctx:
#     ctx.prec = 10                    # устанавливаем 10 знаков после запятой
#     print(num1 / num2)

# import os
#
# with os.scandir('./../6_1') as entries:
#     for entry in entries:
#         print(entry.name, '--->', entry.stat().st_size, 'bytes')

from tempfile import TemporaryFile

with TemporaryFile(mode='r+') as file:
    file.write('Python generation!')
    file.seek(0)
    content = file.read()
    print(content)








