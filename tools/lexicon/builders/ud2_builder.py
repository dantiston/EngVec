#!/usr/bin/env python3.6

import argparse

from .conll_builder import ConllBuilder
from matrix_lexicon import LexiconType, MatrixLexicalItem


TAG_MAPPINGS = {
    "NOUN": (LexiconType.COUNT_NOUNS, "noun"),
    "PRON": (LexiconType.PRONOUNS, "pronoun"),
    "PROPN": (LexiconType.PROPER_NOUNS, "proper-noun"),
    "VERB": (LexiconType.TRANSITIVE_VERBS, "verb"),
    "AUX": (LexiconType.AUXILIARIES, "auxiliaries"),
    "ADJ": (LexiconType.ADJECTIVES, "adjective"),
    "ADP": (LexiconType.PREPOSITIONS, "preposition"),
    "NUM": (LexiconType.DETERMINERS, "determiner"),
    "DET": (LexiconType.DETERMINERS, "determiner"),
    "PART": (LexiconType.COMPLEMENTIZERS, "complementizer"),
    "PUNCT": (LexiconType.PUNCTUATION, "punctuation"),
    "SYM": (LexiconType.PUNCTUATION, "punctuation"),
    "SCONJ": (LexiconType.CONJUNCTIONS, "subordinating-conjunction"),
    "CCONJ": (LexiconType.CONJUNCTIONS, "coordinating-conjunction"),
    "ADV": (LexiconType.ADVERBS, "adverbs"),
    "X": (LexiconType.OTHER, "unknown"),
    "INTJ": (LexiconType.INTERJECTION, "discourse-particle"),
}


class UniversalDependencies2Builder(ConllBuilder):

    def __init__(self):
        super().__init__()


    def get_name(self):
        return "UniversalDependencies2Builder"


    def set_args(self, parser: argparse.ArgumentParser) -> None:
        super().set_args(parser)
        parser.add_argument("--ud2-conll-files", required=True, nargs="+", help="Directory of files containing Universal Dependencies 2.0 CONLL format files")


    def build(self, options) -> None:
        for path in options.ud2_conll_files:
            self.instances.extend(self.process_conll_file(path))

        for instance in self.instances:
            for token in instance:
                key, typeName = TAG_MAPPINGS[token.pos]
                value = MatrixLexicalItem(token.token, token.lemma)
                self.lexicon.add(key, typeName, value)
