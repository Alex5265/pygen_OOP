# Класс FuzzyString
# Реализуйте класс FuzzyString, наследника класса str, описывающий строку, которая при любых сравнениях (==, !=, >, <, >=, <=) и проверках на принадлежность (in, not in) не учитывает регистр. Процесс создания экземпляра класса FuzzyString должен совпадать с процессом создания экземпляра класса str.
#
# Примечание 1. Если объект, с которым выполняется операция сравнения, некорректен, метод, реализующий эту операцию, должен вернуть константу NotImplemented.
#
# Примечание 2. Никаких ограничений касательно реализации класса FuzzyString нет, она может быть произвольной.


class FuzzyString(str):
    def __new__(cls, string):
        return super().__new__(cls, string.lower())

    @staticmethod
    def _not_string(other):
        return not isinstance(other, str)

    def __eq__(self, other):
        if self._not_string(other):
            return NotImplemented
        return super().__eq__(other.lower())

    def __ne__(self, other):
        if self._not_string(other):
            return NotImplemented
        return super().__ne__(other.lower())

    def __lt__(self, other):
        if self._not_string(other):
            return NotImplemented
        return super().__lt__(other.lower())

    def __gt__(self, other):
        if self._not_string(other):
            return NotImplemented
        return super().__gt__(other.lower())

    def __le__(self, other):
        if self._not_string(other):
            return NotImplemented
        return super().__le__(other.lower())

    def __ge__(self, other):
        if self._not_string(other):
            return NotImplemented
        return super().__ge__(other.lower())

    def __contains__(self, item):
        return super().__contains__(item.lower())


s1 = FuzzyString('BeeGeek')
s2 = FuzzyString('beegeek')

print(s1 == s2)
print(s1 in s2)
print(s2 in s1)
print(s2 not in s1)






