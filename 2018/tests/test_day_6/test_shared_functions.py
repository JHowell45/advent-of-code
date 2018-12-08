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
