class UpperCaseDict(dict):
    def __setitem__(self, key, value):
        key = str(key).upper()
        super().__setitem__(key, value)

    def __repr__(self):
        return f'{type(self).__name__}({super().__repr__()})'


numbers = UpperCaseDict()
numbers['one'] = 1
numbers['two'] = 2

print(numbers)