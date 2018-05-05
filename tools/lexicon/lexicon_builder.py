#!/usr/bin/env python3.6

import argparse

from builders import ud2_corpus_builder


class LexiconBuilder(object):

    def __hash__(self) -> int:
        return hash(self.get_name())


    def get_name(self) -> str:
        raise TypeError("Not implemented")


    def set_args(self, parser: argparse.ArgumentParser) -> None:
        pass


    def registerBuilder(self, builder: 'LexiconBuilder'):
        self.builders.add(builder)


if __name__ == "__main__":

    lexicon_builder = LexiconBuilder()
    builders = {builder() for builder in {ud2_corpus_builder.UniversalDependencies2Builder}}

    parser = argparse.ArgumentParser("Build a Grammar Matrix Lexicon using the specified options")
    for builder in builders:
        builder.set_args(parser)

    args = parser.parse_args()
