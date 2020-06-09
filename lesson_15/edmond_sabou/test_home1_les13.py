import unittest

from lesson_15.edmond_sabou import home1_les13


class TestPoligons(unittest.TestCase):

    def test_if_side_is_not_none(self):
        sides = 1

        i = home1_les13.Polygon(sides)

        self.assertIsNotNone(i, "Value cannot be None!")

    def test_if_value_is_not_string(self):

        i = home1_les13.Polygon(1, 2, 2, 3)

        assert isinstance(i.sides, tuple)

    def test_if_value_is_not_string2(self):

        i = home1_les13.Polygon(1, 2, 2, 3)

        assert all([isinstance(side, int) for side in i.sides])

    def test_if_triangle_has_3_sides(self):
        i = home1_les13.Triangle(1, 2, 3)

        len_sides = len(i.sides)

        self.assertEqual(len_sides, 3, "Triangle must have 3 sides")

    def test_if_square_has_4_sides(self):
        i = home1_les13.Square(1, 2, 3, 4)

        len_sides = len(i.sides)

        self.assertEqual(len_sides, 4, "Square must have 4 sides")

    def test_if_sides_are_not_negative(self):
        i = home1_les13.Polygon(1, 2, 3, 4, -56)

        self.assertIsNot(i, -56, "Cannot have negative values")


if __name__ == "__main__":
    unittest.main()
