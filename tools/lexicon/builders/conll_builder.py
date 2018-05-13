#!/usr/bin/env python3.6


import argparse

from typing import List, Tuple

from lexicon_builder import LexiconBuilder
from data_types.conll import ConllDocument


class ConllBuilder(LexiconBuilder):

    def __init__(self):
        super().__init__()
        self.instances = []


    def set_args(self, parser: argparse.ArgumentParser) -> None:
        pass


    def process_conll_file(self, path):
        instances = []
        with open(path, 'r', encoding="UTF-8") as f:
            instances = self._load(f)
        return instances


    def _load(self, f) -> List[Tuple[str]]:
        result = []
        current = []
        for line in f:
            line = line.strip()
            if line:
                current.append(line)
            elif current:
                result.append(ConllDocument(current))
                current = []
        if current:
            result.append(ConllDocument(current))
        return result
