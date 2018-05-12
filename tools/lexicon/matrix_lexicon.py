#!/usr/bin/env python3.6

from collections import defaultdict
from enum import Enum, unique
from typing import Dict, Set

@unique
class LexiconType(Enum):
    TRANSITIVE_VERBS = 1
    INTRANSITIVE_VERBS = 2
    DITRANSITIVE_VERBS = 3
    COUNT_NOUNS = 4
    MASS_NOUNS = 5
    PROPER_NOUNS = 6
    ADJECTIVES = 7
    PREPOSITIONS = 8


class MatrixLexicon(object):

    def __init__(self) -> None:
        self.values = defaultdict(lambda: defaultdict(set))


    def get(self, key: LexiconType) -> Dict[str, Set[str]]:
        if type(key) is not LexiconType:
            raise TypeError("Expected LexiconType, received {}".format(type(key)))
        return self.values[key]


    def add(self, key: LexiconType, typeName: str, value: str) -> None:
        if key is None or type(key) is not LexiconType or typeName is None or value is None:
            raise TypeError("MatrixLexicon.add received illegal None type argument")
        self.values[key][typeName].add(value)
