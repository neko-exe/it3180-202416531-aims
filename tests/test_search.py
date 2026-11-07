import unittest

from aims.dvd import DigitalVideoDisc
from aims.search import search_by_title


class TestSearch(unittest.TestCase):
    def test_search_by_title(self):
        items = [DigitalVideoDisc("The Lion King"), DigitalVideoDisc("Aladdin")]
        self.assertEqual(search_by_title(items, "Lion"), [items[0]])
        self.assertEqual(search_by_title(items, "missing"), [])

    def test_search_case_insensitive(self):
        items = [DigitalVideoDisc("The Lion King")]
        self.assertEqual(search_by_title(items, "lion"), items)
        self.assertEqual(search_by_title(items, "LION"), items)
