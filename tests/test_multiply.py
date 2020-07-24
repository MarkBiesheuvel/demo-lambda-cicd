#!/usr/bin/env python

from source.arithmetic import multiply
from unittest import TestCase

class Arithmetic(TestCase):

    def test_small_positive_numbers(self):
        self.assertEqual(multiply(1, 0), 0)
        self.assertEqual(multiply(1, 1), 1)
        self.assertEqual(multiply(1, 2), 2)
        self.assertEqual(multiply(2, 1), 2)
        self.assertEqual(multiply(2, 2), 4)
