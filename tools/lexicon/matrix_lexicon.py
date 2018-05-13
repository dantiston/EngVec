#!/usr/bin/env python3.6

from collections import defaultdict
from enum import Enum, unique
from typing import Dict, Set

@unique
class LexiconType(Enum):
    TRANSITIVE_VERBS = 1
    INTRANSITIVE_VERBS = 2
    DITRANSITIVE_VERBS = 3
    AUXILIARIES = 4
    COUNT_NOUNS = 5
    MASS_NOUNS = 6
    PROPER_NOUNS = 7
    PRONOUNS = 8
    ADJECTIVES = 9
    PREPOSITIONS = 10
    DETERMINERS = 11
    COMPLEMENTIZERS = 12
    PUNCTUATION = 13
    CONJUNCTIONS = 14
    ADVERBS = 15
    OTHER = 16
    INTERJECTION = 17


class MatrixLexicon(object):

    def __init__(self) -> None:
        self.values = defaultdict(lambda: defaultdict(set))


    def get(self, key: LexiconType) -> Dict[str, Set['MatrixLexicalItem']]:
        if type(key) is not LexiconType:
            raise TypeError("Expected LexiconType, received {}".format(type(key)))
        return self.values[key]


    def add(self, key: LexiconType, typeName: str, value: 'MatrixLexicalItem') -> None:
        if type(key) is not LexiconType or typeName is None or type(value) is not MatrixLexicalItem:
            raise TypeError("MatrixLexicon.add received illegal type argument")
        self.values[key][typeName].add(value)


    def to_choices(self) -> str:
        return "<{} choices>".format(self.__len__())


    def __len__(self) -> int:
        return sum(len(s) for key, nested in self.values.items() for s in nested)


class MatrixLexicalItem(object):

    def __init__(self, surface: str, lemma: str):
        if surface == None or lemma == None:
            raise TypeError("MatrixLexicalItem received illegal None parameter")
        self.surface = surface.lower()
        self.lemma = lemma


    def __repr__(self) -> str:
        return "<{},{}>".format(self.surface, self.lemma)


    def __hash__(self):
        return hash((self.surface, self.lemma))


    def __eq__(self, other):
        if type(other) is MatrixLexicalItem:
            return self.surface == other.surface and self.lemma == other.lemma
        return False
