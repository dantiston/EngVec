#!/usr/bin/env python3.6

import argparse

from matrix_lexicon import MatrixLexicon


class LexiconBuilder(object):

    def __init__(self):
        self.builders = []
        self.lexicon = MatrixLexicon()


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


    def to_choices(self) -> str:
        return self.lexicon.to_choices()


if __name__ == "__main__":

    # Circular dependencies must be defined in main
    from builders import ud2_builder

    # TODO: Separate top-level builder from child builders
    # lexicon_builder = LexiconBuilder()
    # builders = {builder() for builder in (ud2_builder.UniversalDependencies2Builder,)}
    lexicon_builder = ud2_builder.UniversalDependencies2Builder()
    builders = {lexicon_builder}

    parser = argparse.ArgumentParser("Build a Grammar Matrix Lexicon using the specified options")
    for builder in builders:
        builder.set_args(parser)

    args = parser.parse_args()

    for builder in builders:
        builder.build(args)

    print(lexicon_builder.to_choices())
