import unittest

from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class TestCartSort(unittest.TestCase):
    def setUp(self):
        self.cart = Cart()
        self.cart.add_dvd(DigitalVideoDisc("B", cost=20))
        self.cart.add_dvd(DigitalVideoDisc("A", cost=30))

    def test_sort_by_title(self):
        self.cart.sort_by_title()
        self.assertEqual([dvd.title for dvd in self.cart.items], ["A", "B"])

    def test_sort_by_cost(self):
        self.cart.sort_by_cost()
        self.assertEqual([dvd.cost for dvd in self.cart.items], [20, 30])
