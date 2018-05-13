#!/usr/bin/env python3.6

import unittest

from matrix_lexicon import MatrixLexicon, LexiconType, MatrixLexicalItem


class MatrixLexiconTests(unittest.TestCase):

    def test_basic(self) -> None:
        lexicon = MatrixLexicon()
        lexicon.add(LexiconType.TRANSITIVE_VERBS, "test", MatrixLexicalItem("hello", "world"))
        actual = lexicon.get(LexiconType.TRANSITIVE_VERBS)
        expected = {"test": {MatrixLexicalItem("hello", "world")}}
        self.assertEqual(actual, expected)


    def test_multiple_values(self) -> None:
        lexicon = MatrixLexicon()
        lexicon.add(LexiconType.TRANSITIVE_VERBS, "test", MatrixLexicalItem("love", "love"))
        lexicon.add(LexiconType.TRANSITIVE_VERBS, "test", MatrixLexicalItem("hate", "hate"))
        actual = lexicon.get(LexiconType.TRANSITIVE_VERBS)
        expected = {"test": {MatrixLexicalItem("love", "love"), MatrixLexicalItem("hate", "hate")}}
        self.assertEqual(actual, expected)


    def test_multiple_values_is_set(self) -> None:
        lexicon = MatrixLexicon()
        lexicon.add(LexiconType.TRANSITIVE_VERBS, "test", MatrixLexicalItem("love", "love"))
        lexicon.add(LexiconType.TRANSITIVE_VERBS, "test", MatrixLexicalItem("love", "love"))
        lexicon.add(LexiconType.TRANSITIVE_VERBS, "test", MatrixLexicalItem("hate", "hate"))
        lexicon.add(LexiconType.TRANSITIVE_VERBS, "test", MatrixLexicalItem("hate", "hate"))
        actual = lexicon.get(LexiconType.TRANSITIVE_VERBS)
        expected = {"test": {MatrixLexicalItem("love", "love"), MatrixLexicalItem("hate", "hate")}}
        self.assertEqual(actual, expected)


    def test_multiple_types(self) -> None:
        lexicon = MatrixLexicon()
        lexicon.add(LexiconType.TRANSITIVE_VERBS, "nice", MatrixLexicalItem("love", "love"))
        lexicon.add(LexiconType.TRANSITIVE_VERBS, "mean", MatrixLexicalItem("hate", "hate"))
        actual = lexicon.get(LexiconType.TRANSITIVE_VERBS)
        expected = {"nice": {MatrixLexicalItem("love", "love")}, "mean": {MatrixLexicalItem("hate", "hate")}}
        self.assertEqual(actual, expected)


    def test_multiple_keys(self) -> None:
        lexicon = MatrixLexicon()
        lexicon.add(LexiconType.TRANSITIVE_VERBS, "test", MatrixLexicalItem("love", "love"))
        lexicon.add(LexiconType.INTRANSITIVE_VERBS, "test", MatrixLexicalItem("hate", "hate"))
        actual1 = lexicon.get(LexiconType.TRANSITIVE_VERBS)
        expected1 = {"test": {MatrixLexicalItem("love", "love")}}
        actual2 = lexicon.get(LexiconType.INTRANSITIVE_VERBS)
        expected2 = {"test": {MatrixLexicalItem("hate", "hate")}}
        self.assertEqual(actual1, expected1)
        self.assertEqual(actual2, expected2)


    def test_illegal_key(self) -> None:
        lexicon = MatrixLexicon()
        with self.assertRaises(TypeError):
            lexicon.add("a", "b", "c")


if __name__ == "__main__":
    unittest.main()
