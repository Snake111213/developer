class puntoDerecho(object):

    def get_x(self):
        return self._x

    def set_x(self):
        self._x = abs(x)

    x = property(get_x, set_x)