import unittest

from models.rectangle import Rectangle


class RectangleTest(unittest.TestCase):
    def test_no_args(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle()

    def test_width_height(self):
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)

    def test_width_heigth_id(self):
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_area(self):
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

        r2 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r2.area(), 56)
