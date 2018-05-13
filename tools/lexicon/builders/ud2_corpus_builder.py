#!/usr/bin/env python3.6

import argparse

from .conll_corpus_builder import ConllBuilder


class UniversalDependencies2Builder(ConllBuilder):

    def get_name(self):
        return "UniversalDependencies2Builder"


    def set_args(self, parser: argparse.ArgumentParser) -> None:
        super().set_args(parser)
        parser.add_argument("--ud2-conll-files", required=True, nargs="+", help="Directory of files containing Universal Dependencies 2.0 CONLL format files")
