from unittest import result


__global_dict = {}

def singleton(name, bases, namespace):
    class Result:pass
    Result.__name__ = name
    Result.__bases__ = bases
    Result.__dict__ = namespace
    __global_dict[Result] = Result()
    return Factory(Result)

class Factory:
    def __init__(self, key):
        self._key = key
    def __call__(self):
        return __global_dict[self._key]

def test():
    class A:
        __metaclass__ = singleton
        def __init__(self):
            self.a=1

    a=A()
    al=A()
    print ("a is al", a is al)
    a.a=12
    a2=A()

    print('a.a == a2.a == 12', a.a == a2.a == 12)
    class B:
        __metaclass__ = singleton
    b=B()
    a=A()
    print('a is b', a==b)