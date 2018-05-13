#!/usr/bin/env python3.6

import unittest

from builders.conll_builder import ConllBuilder


class ConllBuilderLoadTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_builder = ConllBuilder()


    def test_basic(self):
        actual = ConllBuilderLoadTests.test_builder._load(["abc"])
        expected = [("abc",)]
        self.assertEqual(actual, expected)


    def test_none(self):
        actual = ConllBuilderLoadTests.test_builder._load([])
        expected = []
        self.assertEqual(actual, expected)


    def test_multiple(self):
        actual = ConllBuilderLoadTests.test_builder._load(["abc", "", "def"])
        expected = [("abc",), ("def",)]
        self.assertEqual(actual, expected)


    def test_extra_whitespace(self):
        actual = ConllBuilderLoadTests.test_builder._load(["", "abc", ""])
        expected = [("abc",)]
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
