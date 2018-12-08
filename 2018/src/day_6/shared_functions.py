from pprint import pprint
from string import ascii_lowercase


class ParsePoints:
    def __init__(self, string_rep, point_id=None):
        self.id = point_id
        self.x = string_rep
        self.y = string_rep
        self.close_points = {(self.x, self.y)}

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, new_points_id):
        self._id = None if new_points_id is None else str(new_points_id)

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, new_x_point):
        if isinstance(new_x_point, int):
            self._x = new_x_point
        else:
            self._x = int(new_x_point.split(",")[0].strip())

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, new_y_point):
        if isinstance(new_y_point, int):
            self._y = new_y_point
        else:
            self._y = int(new_y_point.split(",")[1].strip())

    @property
    def geo_points(self):
        return (self.y, self.x)

    @geo_points.setter
    def geo_points(self, new_geo_points):
        self.y = new_geo_points[0]
        self.x = new_geo_points[1]

    @property
    def close_points(self):
        return self._close_points

    @close_points.setter
    def close_points(self, new_close_points):
        if isinstance(new_close_points, set):
            self._close_points = new_close_points
        else:
            self._close_points = {new_close_points}

    def add_close_point(self, close_point):
        if isinstance(close_point, tuple):
            self._close_points.add(close_point)
        else:
            raise TypeError(
                "The 'close_point' is of the incorrect type. "
                "Should be of type '{}' and not '{}'".format('tuple', type(close_point))
            )

    @property
    def get_number_of_closest_points(self):
        return len(self.close_points)

    @staticmethod
    def generate_parsed_points(points):
        alphabet = list(ascii_lowercase)
        for index, point in enumerate(points):
            yield ParsePoints(point, alphabet[index].upper())

    def __repr__(self):
        return (
            "<ParsePoints ID: {}, X: {}, Y: {}, Number of Closest Points: {}>".format(
                self.id, self.x, self.y, self.get_number_of_closest_points
            )
        )


class Manhatten:
    def __init__(self, points):
        self.points = points
        self.x_points = points
        self.y_points = points

    @property
    def points(self):
        return self._points

    @points.setter
    def points(self, new_points):
        self._points = {
            point.id: point for point in ParsePoints.generate_parsed_points(new_points)
        }

    @property
    def x_points(self):
        return self._x_points

    @x_points.setter
    def x_points(self, new_points):
        self._x_points = set()
        for point in ParsePoints.generate_parsed_points(new_points):
            self._x_points.add(point.x)

    @property
    def min_x(self):
        return min(self.x_points)

    @property
    def max_x(self):
        return max(self.x_points)

    @property
    def y_points(self):
        return self._y_points

    @y_points.setter
    def y_points(self, new_points):
        self._y_points = set()
        for point in ParsePoints.generate_parsed_points(new_points):
            self._y_points.add(point.y)

    @property
    def min_y(self):
        return min(self.y_points)

    @property
    def max_y(self):
        return max(self.y_points)

    @property
    def points_length(self):
        return len(self.points)

    @property
    def graph(self):
        try:
            return self._graph
        except AttributeError:
            self.generate_graph()
            return self._graph

    @property
    def graph_length(self):
        return {"x": len(self.graph[0]), "y": len(self.graph)}

    def generate_graph(self):
        self.__create_base_graph()
        self.__set_points_in_graph()

    def __create_base_graph(self):
        self._graph = []
        for y_index in range(self.max_y + 1):
            self._graph.append([])
            for _ in range(self.max_x + 1):
                self._graph[y_index].append(".")

    def __set_points_in_graph(self):
        for point in self.points.values():
            self._graph[point.y][point.x] = point.id

    def calculate_manhatten_distance(self, first_distance, second_distance):
        return int(
            abs((first_distance[0] - second_distance[0]))
            + abs((first_distance[1] - second_distance[1]))
        )

    def set_closest_points(self, verbose=False):
        self.__create_base_graph()
        self.__set_points_in_graph()
        lengths = self.graph_length
        for y in range(lengths["y"]):
            for x in range(lengths["x"]):
                best_point = "."
                best_distance = (self.graph_length["x"] * self.graph_length["y"]) + 1
                current_point = (y, x)
                if self.graph[y][x] == ".":
                    for point in self.points.values():
                        distance = self.calculate_manhatten_distance(
                            point.geo_points, current_point
                        )
                        if int(distance) < int(best_distance):
                            best_distance = distance
                            best_point = point.id.lower()
                        elif int(distance) == int(best_distance):
                            best_distance = distance
                            best_point = "."
                        if verbose:
                            print(
                                "ID: {}, Points: {}, Distance: {}".format(
                                    point.id, current_point, distance
                                )
                            )
                    if verbose:
                        print("Point choosen: {}\n".format(best_point))
                if best_point != ".":
                    self.graph[y][x] = best_point
                    self.points[best_point.upper()].add_close_point(current_point)
                # pprint(self.graph)
        pprint(self.points)

    def get_edge_points(self):
        inf_points = set()
        x_min = 0
        y_min = 0
        lengths = self.graph_length
        x_max = lengths["x"] - 1
        y_max = lengths["y"] - 1
        for y_index in [y_min, y_max]:
            for x_index in range(x_max):
                value = self.graph[y_index][x_index].upper()
                if value != ".":
                    inf_points.add(value)
        for x_index in [x_min, x_max]:
            for y_index in range(y_max):
                value = self.graph[y_index][x_index].upper()
                if value != ".":
                    inf_points.add(value)
        return inf_points

    def get_largest_distance(self):
        points_to_remove = self.get_edge_points()
        all_points = self.points
        for delete_point in points_to_remove:
            del all_points[delete_point]
        return max(
            [
                getattr(point, "get_number_of_closest_points")
                for point in all_points.values()
            ]
        )

    def __repr__(self):
        return "<Manhatten Points: {}, X: {}, Y: {}, Length: {}>".format(
            self.points, self.x_points, self.y_points, self.points_length
        )
