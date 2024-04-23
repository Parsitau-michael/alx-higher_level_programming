import unittest

from models.base import Base


class TestBase(unittest.TestCase):
    def test_single_obj_creation(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_specific_id(self):
        b1 = Base(20)
        self.assertEqual(b1.id, 20)

    def test_multiple_obj_creation(self):
        b1 = Base()
        b2 = Base()
        b3 = Base(12)
        b4 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 12)
        self.assertEqual(b4.id, 3)
