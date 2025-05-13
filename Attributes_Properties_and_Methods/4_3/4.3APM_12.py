# Класс Todo
# Реализуйте класс Todo, описывающий список дел. При создании экземпляра класс не должен принимать никаких аргументов.
#
# Экземпляр класса Todo должен иметь один атрибут:
#
# things — изначально пустой список дел, которые нужно выполнить
# Класс Todo должен иметь четыре метода экземпляра:
#
# add() — метод, принимающий название дела и его приоритет (целое число) и добавляющий данное дело в список дел в виде кортежа:
# (<название дела>, <приоритет>)
# get_by_priority() — метод, принимающий в качестве аргумента целое число n и возвращающий список названий дел, имеющих приоритет n
# get_low_priority() — метод, возвращающий список названий дел, имеющих самый низкий приоритет
# get_high_priority() — метод, возвращающий список названий дел, имеющих самый высокий приоритет
# Примечание 1. Названия дел в списках, возвращаемых методами get_by_priority(), get_low_priority() и get_high_priority(), должны располагаться в том порядке, в котором они были добавлены в список.
#
# Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.


class Todo:
    def __init__(self):
        self.things = []

    def add(self, things, priority):
        self.things.append((things, priority))

    def get_by_priority(self, priority):
        return [i[0] for i in self.things if i[1] == priority]

    def get_low_priority(self):
        if not self.things:
            return self.things
        priority = min(map(lambda x: x[1], self.things))
        return self.get_by_priority(priority)


    def get_high_priority(self):
        if not self.things:
            return self.things
        priority = max(map(lambda x: x[1], self.things))
        return self.get_by_priority(priority)





todo = Todo()

todos = [
    'Выбрать хостинг для своего сайта',
    'Записаться к стоматологу',
    'Записаться на курсы английского',
    'Навести порядок на кухне',
    'Подготовить одежду к лету',
    'Подготовиться к выступлению в понедельник',
    'Помыть машину',
    'Пропылесосить ковры',
    'Свозить Кемаля к ветеринару',
    'Сходить в парикмахерскую',
    'Посетить выставку камней'
]

priorities = [4, 1, 2, 5, 2, 5, 5, 3, 3, 3, 4]
for t, p in zip(todos, priorities):
    todo.add(t, p)

print(todo.things)
print(todo.get_by_priority(3))
print(todo.get_low_priority())
print(todo.get_high_priority())
