#!/usr/bin/env python3.6

import unittest

from builders.conll_builder import ConllBuilder
from data_types.conll import ConllDocument


class ConllBuilderLoadTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_builder = ConllBuilder()


    def test_basic(self):
        actual = ConllBuilderLoadTests.test_builder._load(["1\tabc\tabc\t_\t_"])
        expected = [ConllDocument(["1\tabc\tabc\t_\t_"])]
        self.assertEqual(actual, expected)


    def test_none(self):
        actual = ConllBuilderLoadTests.test_builder._load([])
        expected = []
        self.assertEqual(actual, expected)


    def test_multiple(self):
        actual = ConllBuilderLoadTests.test_builder._load(["1\tabc\tabc\t_\t_", "", "1\tdef\tdef\t_\t_"])
        expected = [ConllDocument(["1\tabc\tabc\t_\t_"]), ConllDocument(["1\tdef\tdef\t_\t_"])]
        self.assertEqual(actual, expected)


    def test_extra_whitespace(self):
        actual = ConllBuilderLoadTests.test_builder._load(["", "1\tabc\tabc\t_\t_", ""])
        expected = [ConllDocument(["1\tabc\tabc\t_\t_"])]
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
