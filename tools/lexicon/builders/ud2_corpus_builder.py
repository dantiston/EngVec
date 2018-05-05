#!/usr/bin/env python3.6

import argparse
from builders.conll_corpus_builder import ConllBuilder


class UniversalDependencies2Builder(ConllBuilder):

    def __init__(self):
        super()


    def get_name(self):
        return "UniversalDependencies2Builder"


    def build(self, options) -> None:
        self.process_conll_file(options.universal_dependencies_file)


    def set_args(self, parser: argparse.ArgumentParser) -> None:
        super().set_args(parser)
        parser.add_argument("--ud2-conll-files", help="Directory of files containing Universal Dependencies 2.0 CONLL format files")
