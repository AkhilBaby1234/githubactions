from main import increment
from unittest import TestCase


class IncrementTest(TestCase):

    def test_increment(self):
        result = increment(10, 8)
        self.assertEqual(result, 18)
