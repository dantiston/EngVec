#!/usr/bin/env python3.6

import argparse


class LexiconBuilder(object):

    def __init__(self):
        self.builders = []


    def __hash__(self) -> int:
        return hash(self.get_name())


    def __str__(self) -> str:
        return self.get_name()


    def __repr__(self) -> str:
        return "<{}>".format(self.get_name())


    def get_name(self) -> str:
        raise TypeError("Not implemented")


    def set_args(self, parser: argparse.ArgumentParser) -> None:
        pass


    def registerBuilder(self, builder: 'LexiconBuilder'):
        self.builders.add(builder)


    def process(self):
        raise NotImplementedError()


if __name__ == "__main__":

    # Circular dependencies must be defined in main
    from builders import ud2_corpus_builder

    lexicon_builder = LexiconBuilder()
    builders = {builder() for builder in (ud2_corpus_builder.UniversalDependencies2Builder,)}

    parser = argparse.ArgumentParser("Build a Grammar Matrix Lexicon using the specified options")
    for builder in builders:
        builder.set_args(parser)

    args = parser.parse_args()

    for builder in builders:
        builder.build(args)
