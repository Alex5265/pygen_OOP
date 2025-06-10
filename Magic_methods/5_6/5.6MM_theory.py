class Cat:
    def __init__(self, name):
        self.name = name                   # имя кошки

    def __call__(self):
        print('Меня зовут', self.name)


cat = Cat('Кемаль')

cat()

class Cat:
    def __init__(self, name):
        self.name = name

    def __call__(self, speech):
        print('Меня зовут', self.name, 'и я делаю', speech)


cat = Cat('Кемаль')

cat('Мяу')                                 # равнозначно cat.__call__('Мяу')
cat('Мяяяяяy')                             # равнозначно cat.__call__('Мяяяяяy')

def line_generator(k, b):
    def func(x):
        return k * x + b
    return func

line_func1 = line_generator(2, 5)          # получаем функцию y = 2*x + 5
line_func2 = line_generator(-6, 9)         # получаем функцию y = -6*x + 9

print(line_func1(10))                      # выводим значение 2*10 + 5 = 25
print(line_func2(4))                       # выводим значение -6*4 + 9 = -15

class LineGenerator:
    def __init__(self, k, b):
        self.k = k
        self.b = b

    def __call__(self, x):
        return self.k * x + self.b


line_func1 = LineGenerator(2, 5)           # получаем функцию y = 2*x + 5
line_func2 = LineGenerator(-6, 9)          # получаем функцию y = -6*x + 9

print(line_func1(10))                      # выводим значение 2*10 + 5 = 25
print(line_func2(4))                       # выводим значение -6*4 + 9 = -15

















