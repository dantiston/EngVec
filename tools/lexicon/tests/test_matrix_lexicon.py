#!/usr/bin/env python3.6

import unittest

from matrix_lexicon import MatrixLexicon, LexiconType


class MatrixLexiconTests(unittest.TestCase):

    def test_basic(self) -> None:
        lexicon = MatrixLexicon()
        lexicon.add(LexiconType.TRANSITIVE_VERBS, "test", "hello world")
        actual = lexicon.get(LexiconType.TRANSITIVE_VERBS)
        expected = {"test": {"hello world"}}
        self.assertEqual(actual, expected)


    def test_multiple_values(self) -> None:
        lexicon = MatrixLexicon()
        lexicon.add(LexiconType.TRANSITIVE_VERBS, "test", "love")
        lexicon.add(LexiconType.TRANSITIVE_VERBS, "test", "hate")
        actual = lexicon.get(LexiconType.TRANSITIVE_VERBS)
        expected = {"test": {"love", "hate"}}
        self.assertEqual(actual, expected)


    def test_multiple_values_is_set(self) -> None:
        lexicon = MatrixLexicon()
        lexicon.add(LexiconType.TRANSITIVE_VERBS, "test", "love")
        lexicon.add(LexiconType.TRANSITIVE_VERBS, "test", "love")
        lexicon.add(LexiconType.TRANSITIVE_VERBS, "test", "hate")
        lexicon.add(LexiconType.TRANSITIVE_VERBS, "test", "hate")
        actual = lexicon.get(LexiconType.TRANSITIVE_VERBS)
        expected = {"test": {"love", "hate"}}
        self.assertEqual(actual, expected)


    def test_multiple_types(self) -> None:
        lexicon = MatrixLexicon()
        lexicon.add(LexiconType.TRANSITIVE_VERBS, "nice", "love")
        lexicon.add(LexiconType.TRANSITIVE_VERBS, "mean", "hate")
        actual = lexicon.get(LexiconType.TRANSITIVE_VERBS)
        expected = {"nice": {"love"}, "mean": {"hate"}}
        self.assertEqual(actual, expected)
