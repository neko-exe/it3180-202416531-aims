import unittest

from aims.cart import Cart, MAX_NUMBERS_ORDERED
from aims.dvd import DigitalVideoDisc


class TestCart(unittest.TestCase):
    def test_add_dvd_until_full(self):
        cart = Cart()
        for i in range(MAX_NUMBERS_ORDERED):
            self.assertTrue(cart.add_dvd(DigitalVideoDisc(f"DVD {i}")))
        self.assertFalse(cart.add_dvd(DigitalVideoDisc("DVD 21")))
        self.assertEqual(len(cart.items), MAX_NUMBERS_ORDERED)

    def test_discounted_total(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("A", cost=100))
        self.assertEqual(cart.total_cost(), 100)
        self.assertEqual(cart.total_cost_with_discount(20), 80)

    def test_discount_percent_out_of_range(self):
        cart = Cart()
        for percent in (-1, 150):
            with self.subTest(percent=percent):
                with self.assertRaises(ValueError):
                    cart.total_cost_with_discount(percent)
