# -*- coding: utf-8 -*-

def search4prepositions_zhs(phrase: str) -> set:
    """Return any prepositions found in a supplied phrase."""
    # Source http://xh.5156edu.com/page/z3033m4876j18636.html
    # Source https://resources.allsetlearning.com/chinese/grammar/Preposition
    PREPOSITION_zhs = set('')
    return PREPOSITION_zhs.intersection(set(phrase))

def search4letters(phrase: str, letters: str='') -> set:
    """Return a set of the 'letters' found in 'phrase'."""
    return set(letters).intersection(set(phrase))
