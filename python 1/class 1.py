class punto(object):
    def __init__(self, x = 0, y = 0):
        self.set_x(x)
        self.set_y(y)

    def x(self):
        return self._x

    def y(self):
        return self._y

    def set_x(self, x):
        self._x=x

    def set_y(self, y):
        self._y=y