import unittest

from aims.dvd import DigitalVideoDisc
from aims.search import search_by_category, search_by_title


class TestSearch(unittest.TestCase):
    def test_search_by_category(self):
        items = [
            DigitalVideoDisc("The Lion King", category="Animation"),
            DigitalVideoDisc("Star Wars", category="Science Fiction"),
        ]
        self.assertEqual(search_by_category(items, "Animation"), [items[0]])

    def test_search_by_title(self):
        items = [DigitalVideoDisc("The Lion King"), DigitalVideoDisc("Aladdin")]
        self.assertEqual(search_by_title(items, "Lion"), [items[0]])
        self.assertEqual(search_by_title(items, "missing"), [])
