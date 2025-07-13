# Классы LeftParagraph и RightParagraph
# Будем называть словом любую последовательность из одной или более латинских букв.
#
# 1. Реализуйте класс LeftParagraph, описывающий абзац, выровненный по левому краю. При создании экземпляра класс должен принимать один аргумент:
#
# length — длина строки абзаца
# Класс LeftParagraph должен иметь два метода экземпляра:
#
# add() — метод, принимающий в качестве аргумента слово или несколько слов, разделенных пробелом, и добавляющий их в текущий абзац. Если слово не помещается на текущей строке, оно переносится на следующую. Также метод должен автоматически добавлять один пробел после каждого добавленного слова (кроме последнего)
# end() — метод, печатающий текущий абзац, выровненный по левому краю. После вызова метода текущий абзац считается пустым, то есть начинается формирование нового
# 2. Также реализуйте класс RightParagraph, описывающий абзац, выровненный по правому краю. При создании экземпляра класс должен принимать один аргумент:
#
# length — длина строки абзаца
# Класс RightParagraph должен иметь два метода экземпляра:
#
# add() — метод, принимающий в качестве аргумента слово или несколько слов, разделенных пробелом, и добавляющий их в текущий абзац. Если слово не помещается на текущей строке, оно переносится на следующую. Также метод должен автоматически добавлять один пробел после каждого добавленного слова (кроме последнего)
# end() — метод, печатающий текущий абзац, выровненный по правому краю с учетом длины строки. После вызова метода текущий абзац считается пустым, то есть начинается формирование нового
# Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованные классы используются только с корректными данными.
#
# Примечание 2. Никаких ограничений касательно реализаций классов нет, они могут быть произвольными.

from abc import ABC, abstractmethod


class Paragraph(ABC):
    def __init__(self, length):
        self._size = length
        self._paragraph = ['']

    def add(self, words):
        words = words.split()
        for word in words:
            if len(self._paragraph[-1] + f' {word}') > self._size:
                self._paragraph.append('')
            self._paragraph[-1] = (self._paragraph[-1] + f' {word}').lstrip()

    @abstractmethod
    def end(self):
        pass


class LeftParagraph(Paragraph):
    def end(self):
        for line in self._paragraph:
            print(line)
        self._paragraph = ['']


class RightParagraph(Paragraph):
    def end(self):
        for line in self._paragraph:
            print(line.rjust(self._size))
        self._paragraph = ['']



leftparagraph = LeftParagraph(10)

leftparagraph.add('death')
leftparagraph.add('can have me')
leftparagraph.add('when it earns me')
leftparagraph.end()
print()

rightparagraph = RightParagraph(10)

rightparagraph.add('death')
rightparagraph.add('can have me')
rightparagraph.add('when it earns me')
rightparagraph.end()




