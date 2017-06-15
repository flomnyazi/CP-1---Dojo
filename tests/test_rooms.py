import unittest
from rooms import Room


class TestRoom(unittest.TestCase):
    def test_create_room(self):
        self.assertEqual(self.room, Room)

    def test_new_room_type(self):
        self.asserEqual(self.room.type, 'office' or 'livingspace')

    def test_new_room_name(self):
        self.assertEqual(self.room.name,)

    def test_new_room_occupants(self):
        self.assertEqual(self.room.no_of_occupants, 0)
