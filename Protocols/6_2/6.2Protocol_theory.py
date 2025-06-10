class Order:
    def __init__(self, cart, customer):
        self.cart = list(cart)
        self.customer = customer

    def check_key(self, key):                   # отдельный метод для проверки индекса на корректность
        if not isinstance(key, int):
            raise TypeError('Индекс должен быть целым числом')
        if key < 0 or key >= len(self.cart):
            raise IndexError('Неверный индекс')
        return key

    def __len__(self):
        return len(self.cart)

    def __getitem__(self, key):
        key = self.check_key(key)
        return self.cart[key]

    def __contains__(self, item):
        return item in self.cart

    def __iter__(self):
        yield from self.cart

    def __setitem__(self, key, value):
        key = self.check_key(key)
        self.cart[key] = value

    def __delitem__(self, key):
        key = self.check_key(key)
        del self.cart[key]


order = Order(['банан', 'яблоко', 'лимон'], 'Кемаль')

print(*order, sep=', ')

order[1] = 'ананас'
del order[2]

print(*order, sep=', ')
print()


order = Order(['банан', 'яблоко', 'лимон'], 'Кемаль')

print(len(order))
print(order[1])
print('дыня' in order)
print('лимон' in order)
print(*order, sep=', ')


nums = [1, 2, 3, 4, 5]

print(nums[slice(1, None, None)])               # равнозначно nums[1:]
print(nums[slice(3)])                           # равнозначно nums[:3]
print(nums[slice(1, 3)])                        # равнозначно nums[1:3]
print(nums[slice(1, 4, 2)])                     # равнозначно nums[1:4:2]