class Day:
    def __get__(self, obj, obj_type):
        return 50

class A:
    x = Day()
a = A()
a.__dict__['x'] = 20
print(a.x)
