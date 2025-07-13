# Иерархия классов 🔠
# С помощью наследования и приведенной ниже схемы постройте иерархию пустых классов:


class A:
    pass

class C(A):
    pass

class B(A):
    pass

class D(A):
    pass

class E(B, D):
    pass


print(issubclass(E, B))
print(issubclass(E, C))
print(issubclass(E, D))
print()


print(issubclass(B, A))
print(issubclass(C, A))
print(issubclass(D, A))









