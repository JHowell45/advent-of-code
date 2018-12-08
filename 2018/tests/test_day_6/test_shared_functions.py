import pytest


class TestParsePoints:
    def test_id_type(self, parse_points_class):
        assert parse_points_class.id is None

    def test_id_value(self, parse_points_class):
        assert parse_points_class.id is None

    def test_add_id_type(self, parse_points_class):
        parse_points_class.id = "A"
        assert isinstance(parse_points_class.id, str)

    def test_add_id_value(self, parse_points_class):
        parse_points_class.id = "A"
        assert parse_points_class.id == "A"

    def test_x_type(self, parse_points_class):
        assert isinstance(parse_points_class.x, int)

    def test_x_value(self, parse_points_class, x_parse_point_value):
        assert parse_points_class.x == x_parse_point_value

    @pytest.mark.parametrize("x", ["x_parse_point_value", "parse_point_string"])
    def test_add_x_type(self, parse_points_class, x, request, x_parse_point_value):
        parse_points_class.x = request.getfixturevalue(x)
        assert isinstance(parse_points_class.x, int)

    @pytest.mark.parametrize("x", ["x_parse_point_value", "parse_point_string"])
    def test_add_x_value(self, parse_points_class, x, request, x_parse_point_value):
        parse_points_class.x = request.getfixturevalue(x)
        assert parse_points_class.x == x_parse_point_value

    def test_y_type(self, parse_points_class):
        assert isinstance(parse_points_class.y, int)

    def test_y_value(self, parse_points_class, y_parse_point_value):
        assert parse_points_class.y == y_parse_point_value

    @pytest.mark.parametrize("y", ["y_parse_point_value", "parse_point_string"])
    def test_add_y_type(self, parse_points_class, y, request):
        parse_points_class.y = request.getfixturevalue(y)
        assert isinstance(parse_points_class.y, int)

    @pytest.mark.parametrize("y", ["y_parse_point_value", "parse_point_string"])
    def test_add_y_value(self, parse_points_class, y, request, y_parse_point_value):
        parse_points_class.y = request.getfixturevalue(y)
        assert parse_points_class.y == y_parse_point_value

    def test_geo_points_type(self, parse_points_class):
        assert isinstance(parse_points_class.geo_points, tuple)

    def test_geo_points_value(
        self, parse_points_class, y_parse_point_value, x_parse_point_value
    ):
        assert parse_points_class.geo_points == (
            y_parse_point_value,
            x_parse_point_value,
        )

    def test_add_geo_points_type(
        self, parse_points_class, y_parse_point_value, x_parse_point_value
    ):
        parse_points_class.geo_points = (y_parse_point_value, x_parse_point_value)
        assert isinstance(parse_points_class.geo_points, tuple)

    def test_add_geo_points_value(
        self, parse_points_class, y_parse_point_value, x_parse_point_value
    ):
        parse_points_class.geo_points = (y_parse_point_value, x_parse_point_value)
        assert parse_points_class.geo_points == (
            parse_points_class.y,
            parse_points_class.x,
        )

    def test_close_points_type(self, parse_points_class):
        assert isinstance(parse_points_class.close_points, set)

    def test_close_points_value(
        self, parse_points_class, y_parse_point_value, x_parse_point_value
    ):
        assert parse_points_class.close_points == {
            (x_parse_point_value, y_parse_point_value)
        }

    def test_add_close_points_type(
        self, parse_points_class, y_parse_point_value, x_parse_point_value
    ):
        parse_points_class.close_points = {(x_parse_point_value, y_parse_point_value)}
        assert isinstance(parse_points_class.close_points, set)

    def test_add_close_points_value(
        self, parse_points_class, y_parse_point_value, x_parse_point_value
    ):
        parse_points_class.close_points = {(x_parse_point_value, y_parse_point_value)}
        assert parse_points_class.close_points == {
            (parse_points_class.x, parse_points_class.y)
        }
