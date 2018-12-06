"""Use this functions to complete the day 5 puzzle 1 challenge."""


class ParsePoints:
    def __init__(self, string_rep):
        self.x = string_rep
        self.y = string_rep

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, new_x_point):
        self._x = int(new_x_point.split(",")[0].strip())

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, new_y_point):
        self._y = int(new_y_point.split(",")[1].strip())

    def __repr__(self):
        return '<ParsePoints X: {}, Y: {}>'.format(self.x, self.y)


def get_largest_distance(data):
    graph = []
    for point in data:
        coord = ParsePoints(point)
        print(coord)
    return graph
