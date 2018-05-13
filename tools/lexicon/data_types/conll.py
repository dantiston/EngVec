#!/bin/env python3.6

from typing import Dict, List, Tuple


COMMENT = "#"
EMPTY = "_"


class ConllToken(object):

    INDEX, TOKEN, LEMMA, POS, XPOS, MORPH, HEAD, REL, EDEP, MISC = range(10)

    def __init__(self, *args):
        # index, token, lemma, pos, xpos, morph, head, rel, edep, misc
        self.index = str(self.__get_nullable(args, ConllToken.INDEX))
        self.token = args[ConllToken.TOKEN]
        self.lemma = args[ConllToken.LEMMA]
        self.pos = self.__get_nullable(args, ConllToken.POS)
        self.xpos = self.__get_nullable(args, ConllToken.XPOS)

        if len(args) > ConllToken.MORPH:
            self.morph = self._load_dict(self.__get_nullable(args, ConllToken.MORPH))
            self.head = str(self.__get_nullable(args, ConllToken.HEAD))
            self.rel = self.__get_nullable(args, ConllToken.REL)

            if len(args) > ConllToken.EDEP:
                self.edep = self._load_dict(self.__get_nullable(args, ConllToken.EDEP), value_sep=":")
                self.misc = self.__get_nullable(args, ConllToken.MISC)
                self.space_after = "SpaceAfter=No" not in self.misc if self.misc else None

            else:
                self.edep = {}
                self.misc = None
                self.space_after = False

        else:
            self.morph = {}
            self.head = None
            self.rel = None


    @classmethod
    def fromString(cls, string):
        return cls(*string.split("\t"))


    def _load_dict(self, string: str, part_sep: str = "|", value_sep: str = "=") -> Dict[str, str]:
        result = {}
        if string:
            for part in string.split(part_sep):
                try:
                    key, value = part.split(value_sep, 1)
                except Exception:
                    import pdb; pdb.set_trace()
                result[key] = value
        return result


    def __hash__(self) -> int:
        return hash((self.index, self.token, self.lemma, self.pos, self.morph, self.head, self.rel))


    def __eq__(self, other) -> bool:
        if type(other) is ConllToken:
            return self.index == other.index and \
                   self.token == other.token and \
                   self.lemma == other.lemma and \
                   self.pos == other.pos and \
                   self.morph == other.morph and \
                   self.head == other.head and \
                   self.rel == other.rel
        return False


    # TODO: Make this compatible with loading
    def __str__(self) -> str:
        return "\t".join(map(self._as_loadable, (self.index, self.token, self.lemma, self.pos, self.xpos, self.morph, self.head, self.rel)))


    def _as_loadable(self, value):
        if value == EMPTY or value is None:
            return EMPTY
        return value


    def __repr__(self) -> str:
        return "<{}>".format(",".join(map(str, (self.index, self.token, self.lemma, self.pos, self.xpos, self.morph, self.head, self.rel))))


    def __get_nullable(self, args, position):
        value = args[position]
        if value == EMPTY:
            return None
        return value


class ConllDocument(object):

    def __init__(self, lines: List[str]):
        self.lines = lines
        self.metadata = self._load_meta_data(lines)
        self.tokens = self._load_tokens(lines)


    def _load_meta_data(self, lines) -> Dict[str, str]:
        result = {}
        for i, line in enumerate(lines):
            line = line.lstrip()
            if not line.startswith(COMMENT):
                break
            line = line[1:].strip() # Remove comment
            key, value = map(str.strip, line.split("=", 1))
            result[key] = value
        return result


    def _load_tokens(self, lines) -> Tuple[ConllToken, ...]:
        result = []
        for i, line in enumerate(lines):
            line = line.lstrip()
            if not line.startswith(COMMENT):
                line = line.rstrip()
                result.append(ConllToken.fromString(line))
        return tuple(result)


    def __hash__(self) -> int:
        return hash(self.lines)


    def __eq__(self, other) -> bool:
        if type(other) is ConllDocument:
            return self.tokens == other.tokens
        return False


    def __len__(self) -> int:
        return len(self.tokens)


    def __iter__(self):
        return iter(self.tokens)
