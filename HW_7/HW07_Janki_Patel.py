"""
@author: Janki patel
CWID : 10457365
"""

""" this file contain anagrams using list , default dict and counter". Also  we implement all alphabets and web analyzer"""


"""importing some of the in-built functions in python """




from collections import defaultdict, Counter
from typing import Any, Optional, List, DefaultDict, Tuple
def anagrams_lst(str1: str, str2: str) -> bool:
    """ in that we do anagrams using list and return true or false . Also we use sorted for comparing"""

    a1:str = str1.lower()
    a2:str = str2.lower()
    if sorted(list(a1)) == sorted(list(a2)):
        return True
    else:
        return False


def anagrams_dd(str1: str, str2: str) -> bool:
    """in that we do anagrams usind defaultdict return true or false"""
    ana_dd = defaultdict(int)
    """increment  the value store it"""
    s1: str = str1.lower()
    for c in s1:
        ana_dd[c] = ana_dd[c] + 1

    """Decrement the value store it"""
    s2: str = str2.lower()
    for c in s2:
        ana_dd[c] = ana_dd[c] - 1

    """return output """
    output: bool = any(value == 0 for value in ana_dd.values())
    return output


def anagrams_cntr(str1: str, str2: str) -> bool:
    """ in that we do anagrams is using counter and return true or false. we use counter for compare"""

    if Counter(str1.lower()) == Counter(str2.lower()):
        return True
    else:
        return False


def covers_alphabet(sentence: str) -> bool:
    """ in that we do cover the alphabets and return true or false"""
    alpha = "abcdefghijklmnopqrstuvwxyz"
    if (set(sentence.lower()) == set(alpha)) or (set(sentence.lower()) > set(alpha)):
        return True
    else:
        return False


def web_analyzer(weblogs: List[Tuple[str, str]]) -> List[Tuple[str, List[str]]]:
    """in that we do we analyzer and returns the list of values as the input as defaultdict(set)"""
    output = defaultdict(set)
    for i in weblogs:
        name = i[0]
        site = i[1]
        output[site].add(name)
    """return the s"""
    s: bool = sorted([(key, sorted(list(value)))
                     for key, value in output.items()])
    return s
