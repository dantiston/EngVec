#!/bin/env python3.6

import unittest

from data_types import conll


class ConllDocumentTests(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.test_doc = conll.ConllDocument([])


    def test_load_metadata_basic(self):
        actual = ConllDocumentTests.test_doc._load_meta_data(["# key = value"])
        expected = {"key": "value"}
        self.assertEqual(actual, expected)


    def test_load_metadata_multiple(self):
        actual = ConllDocumentTests.test_doc._load_meta_data(["# key = value", "# key2 = value2"])
        expected = {"key": "value", "key2": "value2"}
        self.assertEqual(actual, expected)


    def test_load_metadata_empty(self):
        actual = ConllDocumentTests.test_doc._load_meta_data([])
        expected = {}
        self.assertEqual(actual, expected)


    def test_load_metadata_full(self):
        actual = ConllDocumentTests.test_doc._load_meta_data((
            "# newdoc id = abc",
            "# sent_id = def",
            "# text = I like dogs",
            "1\tI\ti\tPRON\tPRON\t\t2\tnsubj",
            "2\tlike\tlike\tVERB\tVERB\t\t0\troot",
            "3\tdogs\tdog\tNOUN\tNOUN\t\t2\tdobj"))
        expected = {"newdoc id": "abc", "sent_id": "def", "text": "I like dogs"}
        self.assertEqual(actual, expected)


    def test_load_tokens_basic(self):
        actual = ConllDocumentTests.test_doc._load_tokens((
            "1\tI\ti\tPRON\tPRON\t\t2\tnsubj",
            "2\tlike\tlike\tVERB\tVERB\t\t0\troot",
            "3\tdogs\tdog\tNOUN\tNOUN\t\t2\tdobj",
        ))
        expected = (
            conll.ConllToken(1, "I", "i", "PRON", "PRON", "_", 2, "nsubj"),
            conll.ConllToken(2, "like", "like", "VERB", "VERB", "_", 0, "root"),
            conll.ConllToken(3, "dogs", "dog", "NOUN", "NOUN", "_", 2, "dobj"),
        )
        self.assertEqual(actual, expected)


    def test_load_tokens_metadata(self):
        actual = ConllDocumentTests.test_doc._load_tokens((
            "# newdoc id = abc",
            "# sent_id = def",
            "# text = I like dogs",
            "1\tI\ti\tPRON\tPRON\t\t2\tnsubj",
            "2\tlike\tlike\tVERB\tVERB\t\t0\troot",
            "3\tdogs\tdog\tNOUN\tNOUN\t\t2\tdobj",
        ))
        expected = (
            conll.ConllToken(1, "I", "i", "PRON", "PRON", "_", 2, "nsubj"),
            conll.ConllToken(2, "like", "like", "VERB", "VERB", "_", 0, "root"),
            conll.ConllToken(3, "dogs", "dog", "NOUN", "NOUN", "_", 2, "dobj"),
        )
        self.assertEqual(actual, expected)


    def test_init_tokens_basic(self):
        actual = conll.ConllDocument((
            "# newdoc id = abc",
            "# sent_id = def",
            "# text = I like dogs",
            "1\tI\ti\tPRON\tPRON\t\t2\tnsubj",
            "2\tlike\tlike\tVERB\tVERB\t\t0\troot",
            "3\tdogs\tdog\tNOUN\tNOUN\t\t2\tdobj",
        )).tokens
        expected = (
            conll.ConllToken(1, "I", "i", "PRON", "PRON", "_", 2, "nsubj"),
            conll.ConllToken(2, "like", "like", "VERB", "VERB", "_", 0, "root"),
            conll.ConllToken(3, "dogs", "dog", "NOUN", "NOUN", "_", 2, "dobj"),
        )
        self.assertEqual(actual, expected)


    def test_init_metadata_basic(self):
        actual = conll.ConllDocument((
            "# newdoc id = abc",
            "# sent_id = def",
            "# text = I like dogs",
            "1\tI\ti\tPRON\tPRON\t\t2\tnsubj",
            "2\tlike\tlike\tVERB\tVERB\t\t0\troot",
            "3\tdogs\tdog\tNOUN\tNOUN\t\t2\tdobj",
        )).metadata
        expected = {"newdoc id": "abc", "sent_id": "def", "text": "I like dogs"}
        self.assertEqual(actual, expected)


    def test_len(self):
        actual = len(conll.ConllDocument((
            "# newdoc id = abc",
            "# sent_id = def",
            "# text = I like dogs",
            "1\tI\ti\tPRON\tPRON\t\t2\tnsubj",
            "2\tlike\tlike\tVERB\tVERB\t\t0\troot",
            "3\tdogs\tdog\tNOUN\tNOUN\t\t2\tdobj",
        )))
        expected = 3
        self.assertEqual(actual, expected)



if __name__ == "__main__":
    unittest.main()
