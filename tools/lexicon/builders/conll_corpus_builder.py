#!/usr/bin/env python3.6


import argparse
from lexicon_builder import LexiconBuilder

class ConllBuilder(LexiconBuilder):

    def __init__(self):
        super()


    def build(self, options) -> None:
        self.process_conll_file(options.universal_dependencies_file)


    def set_args(self, parser: argparse.ArgumentParser) -> None:
        pass
