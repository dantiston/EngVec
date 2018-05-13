#!/usr/bin/env python3.6


import argparse

from lexicon_builder import LexiconBuilder


class ConllBuilder(LexiconBuilder):

    def __init__(self):
        super()


    def build(self, options) -> None:
        for path in options.ud2_conll_files:
            self.process_conll_file(path)


    def set_args(self, parser: argparse.ArgumentParser) -> None:
        pass


    def process_conll_file(self, path):
        instances = []
        with open(path, 'r') as f:
            instances = self.load(f)
        print(len(instances))
        print(instances[0])


    def load(self, f):
        result = []
        current = []
        for line in f:
            line = line.strip()
            if current and not line:
                result.append(current)
                current = []
            current.append(line)
        if current:
            result.append(current)
        return result
