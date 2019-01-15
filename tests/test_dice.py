#!/usr/bin/env python

from source import dice
from unittest import TestCase

class Dice(TestCase):

    def test_in(self):
        valid_throws = [1, 2, 3, 4, 5, 6]
        for _ in range(1000):
            self.assertIn(dice.throw(), valid_throws)

    def test_less_or_equal(self):
        for _ in range(1000):
            self.assertLessEqual(dice.throw(), 6)

    def test_greater_or_equal(self):
        valid_throws = [1, 2, 3, 4, 5, 6]
        for _ in range(1000):
            self.assertGreaterEqual(dice.throw(), 1)
