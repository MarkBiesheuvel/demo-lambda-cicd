#!/usr/bin/env python

from source.arithmetic import add
from unittest import TestCase

class Arithmetic(TestCase):

    def test_small_positive_numbers(self):
        self.assertEqual(add(1, 0), 1)
        self.assertEqual(add(1, 1), 2)
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(2, 1), 3)
        self.assertEqual(add(2, 2), 4)

    def test_big_positive_numbers(self):
        self.assertEqual(add(1337, 683), 2020)
        self.assertEqual(add(11101, 1011), 12112)

    def test_small_negative_numbers(self):
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(1, -1), 0)
        self.assertEqual(add(-1, -2), -3)
        self.assertEqual(add(-2, 1), -1)
