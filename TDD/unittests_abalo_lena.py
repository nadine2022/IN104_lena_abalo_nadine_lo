import unittest

from zoo import Giraffe, OutOfRangeError


class KnownValues(unittest.TestCase):
    known_values = (
        (
            Giraffe(13, "female", 120, 5.2, 70, 4.0),
            10,
            80
        ),
        (
            Giraffe(13, "female", 120, 5.2, 70, 4.0),
            30,
            100
        ),
        (
            Giraffe(13, "female", 120, 5.2, 10, 4.0),
            10,
            20
        ),
        (
            Giraffe(13, "female", 120, 5.2, 42, 4.0),
            50,
            92
        ),
        (
            Giraffe(13, "female", 120, 5.2, 1, 4.0),
            26,
            27
        )
    )

    def test_add_food_known_values(self):
        """add_food should give known result with known input"""
        for animal, food, known in self.known_values:
            self.assertEqual(known, animal.add_food(food))


class ZooBadInput(unittest.TestCase):

    def test_height_negative(self):
        """get_height should fail with negative input"""
        giraffe = Giraffe(13, "female", 120, -1, 70, 4.0)
        self.assertRaises(OutOfRangeError, giraffe.get_height)

    def test_value_food(self):
        """get_daily_check should fail with negative self.food"""
        giraffe1 = Giraffe(13, "female", 120, 5.2, -1, 4.0)
        self.assertRaises(OutOfRangeError, giraffe1.get_daily_check)

        """get_daily_check should fail with self.food > 100"""
        giraffe2 = Giraffe(13, "female", 120, 5.2, 101, 4.0)
        self.assertRaises(OutOfRangeError, giraffe2.get_daily_check)


if __name__ == "__main__":
    unittest.main()
