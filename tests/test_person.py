import unittest
from person import Person


class TestPerson(unittest.TestCase):
    def test_fellow(self):
        self.assertEqual(self.designation, Fellow)

    def test_staff(self):
        self.asserEqual(self.designation, Staff)
